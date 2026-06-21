"""
Tests targeting every bug in the Bug Reproduction Log (see reflection.md).

These tests encode the EXPECTED (correct) behavior. They are written against
the refactored functions in `logic_utils.py`. Move the logic out of `app.py`
into `logic_utils.py` and fix the bugs until everything here passes.

Assumed signatures (mirroring app.py):
    get_range_for_difficulty(difficulty)         -> (low, high)
    check_guess(guess, secret)                   -> (outcome, message)
    get_attempt_limit_for_difficulty(difficulty) -> int
"""

import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    get_attempt_limit_for_difficulty,
)


# ---------------------------------------------------------------------------
# Bug rows 1-3: the hints are reversed.
#   Input  | Expected   | Actual (bug)
#   399    | Go LOWER!  | Go HIGHER!
#   -10000 | Go HIGHER! | Go LOWER!
#   101    | Go LOWER!  | Go HIGHER!
#
# When the guess is ABOVE the secret you must go LOWER; when it is BELOW the
# secret you must go HIGHER. We check the outcome label AND the direction word
# in the message so a swapped hint string is caught.
# ---------------------------------------------------------------------------

SECRET = 100


def test_guess_399_should_tell_player_to_go_lower():
    outcome, message = check_guess(399, SECRET)
    assert outcome == "Too High"
    assert "lower" in message.lower()
    assert "higher" not in message.lower()


def test_guess_negative_10000_should_tell_player_to_go_higher():
    outcome, message = check_guess(-10000, SECRET)
    assert outcome == "Too Low"
    assert "higher" in message.lower()
    assert "lower" not in message.lower()


def test_guess_101_should_tell_player_to_go_lower():
    outcome, message = check_guess(101, SECRET)
    assert outcome == "Too High"
    assert "lower" in message.lower()
    assert "higher" not in message.lower()


def test_correct_guess_is_a_win():
    outcome, _message = check_guess(SECRET, SECRET)
    assert outcome == "Win"


# ---------------------------------------------------------------------------
# Bug rows 4 & 6: difficulty ranges are wrong.
#   Easy   -> expected 1-20   (bug gave 1-100)
#   Normal -> expected 1-100  (bug gave 1-50)
#   Hard   -> expected 1-50
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "difficulty, expected_range",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 100)),
        ("Hard", (1, 50)),
    ],
)
def test_range_for_difficulty(difficulty, expected_range):
    assert get_range_for_difficulty(difficulty) == expected_range


# ---------------------------------------------------------------------------
# Bug rows 5, 7 & 8: attempt limits are wrong (off by one).
#   Easy   -> expected 6 max attempts (bug gave 5)
#   Normal -> expected 8 max attempts (bug gave 7)
#   Hard   -> expected 5 max attempts (bug gave 4)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "difficulty, expected_attempts",
    [
        ("Easy", 6),
        ("Normal", 8),
        ("Hard", 5),
    ],
)
def test_attempt_limit_for_difficulty(difficulty, expected_attempts):
    assert get_attempt_limit_for_difficulty(difficulty) == expected_attempts

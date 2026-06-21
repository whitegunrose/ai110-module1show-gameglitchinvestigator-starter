def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # Fix: corrected Easy to 1-20 and Normal to 1-100 (ranges were wrong).
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def get_attempt_limit_for_difficulty(difficulty: str):
    """Return the max number of attempts allowed for a given difficulty."""
    # Fix: bumped each limit up by one to undo the off-by-one error.
    limits = {
        "Easy": 6,
        "Normal": 8,
        "Hard": 5,
    }
    return limits.get(difficulty, 8)


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Fix: swapped the hint directions so "too high" tells the player to go LOWER.
    if guess == secret:
        return "Win", "🎉 Correct!"

    # If your guess is ABOVE the secret you need to aim LOWER, and vice versa.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

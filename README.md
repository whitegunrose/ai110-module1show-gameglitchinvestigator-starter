# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
> The game's purpose is to have the user guess a secret number between a bounded range within a certain number of attempts.
- [ ] Detail which bugs you found.
> Some bugs I found consisted of incorrect ranges and incorrect number of attempts for certain difficulties, faulty `new game` button and incorrect output to incorrect guesses.
- [ ] Explain what fixes you applied.
> Some of the fixes I applied to this game was proper handling of guesses that were too high, properly restarting the game witht the `new game` button by tracking the state of the game, and assigning the proper amount of attempts and proper ranges for each difficulty.
## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 399 <!-- Describe this step -->
2. Game returns "Go LOWER!!" <!-- Describe this step -->
3. User enters a guess of -1 -> "Go LOWER!" <!-- Describe this step -->
4. Score correctly updates for higher bound but not lower bound <!-- Describe this step -->
5. Game ends after correct guess or exhausted guess attempts <!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here:
> pytest tests/
> ========================= 10 passed in 0.02s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

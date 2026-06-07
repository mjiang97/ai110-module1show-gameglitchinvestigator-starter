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

- [x] **Game purpose:** A number-guessing game where the player picks a difficulty, then tries to guess a randomly chosen secret number within a limited number of attempts. Hints tell you whether to guess higher or lower after each wrong guess.

- [x] **Bugs found:**
  1. The hint logic was backwards — guessing too low produced "Go lower" and guessing too high produced "Go higher."
  2. The secret number was re-generated on every Streamlit rerun (every button click), so you were never guessing the same target twice.
  3. Clicking "New Game" did not clear state properly — the old guess, win message, and game status all persisted, breaking the new round.
  4. Easy mode displayed a 1–20 range but the secret number was still drawn from 1–100.
  5. The `get_range_for_difficulty` and `update_score` functions existed as stubs in `logic_utils.py` with `NotImplementedError`, while the real implementations sat only in `app.py`.

- [x] **Fixes applied:**
  1. Swapped the comparison operators in `check_guess` so "Too Low" maps to "Go HIGHER" and "Too High" maps to "Go LOWER."
  2. Wrapped secret number generation in `if "secret" not in st.session_state` so it is only created once per game.
  3. Updated the "New Game" handler to reset all relevant session state keys and call `st.rerun()`.
  4. Fixed `get_range_for_difficulty` to actually control the `random.randint` call used when generating the secret.
  5. Moved `get_range_for_difficulty` and `update_score` into `logic_utils.py` and updated `app.py` to import them from there.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

## Summary
Through this Week 2 Tinker activity, the core concept students needed to understand was how to carefully explore and debug AI-generated code rather than assuming it was correct. The exercise emphasized identifying what needs to be fixed, organizing those issues clearly in the code using # FIX ME comments, and tracking changes thoughtfully in the reflection.md file. I think students are most likely to struggle with feeling overwhelmed by multiple files and figuring out how to debug in a structured, step-by-step way. AI was helpful for explaining confusing logic and suggesting possible fixes, but it could be misleading when it confidently proposed solutions before the root cause was fully understood. One important lesson is that students should first reason through what they expect the program to do before relying on AI for a fix. As a TF, I would guide students by asking them to describe the expected versus actual behavior and walk through the code logically to narrow down the issue without giving away the answer.

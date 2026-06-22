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

- The purpose of the game is to let the user guess a randomly generated secret number. The game gives feedback after each guess (“Too High” or “Too Low”) and tracks attempts and score until the user finds the correct number.
- I found several bugs during testing, including inverted hint messages, incorrect score calculation, inconsistent attempt counting, and issues with the new game reset not properly restarting the state. I also noticed type issues where the secret number was sometimes treated as a string instead of an integer, which caused incorrect comparisons.
- To fix these issues, I corrected the hint logic, fixed the score formula, ensured the secret number always stayed an integer, and standardized the attempt counter. I also updated the new game function to properly reset all game state variables, including status, score, and history. Additionally, I refactored the guess-checking logic into a separate logic file and updated tests to match the new function structure.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user starts a new game and the app generates a secret number.
2. The user enters a guess of 40.
3. The game returns "Too Low - Go HIGHER" and decreases the score.
4. The user enters a guess of 70.
5. The game returns "Too High - Go LOWER" and decreases the score.
6. The user enters another guess closer to the secret number.
7. The game updates the attempt counter and score after each guess.
8. The user enters the correct number.
9. The game displays a win message and the final score.
10. The user clicks New Game, and the game resets the secret number, score, attempts, and status correctly.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
platform win32 -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\prati\OneDrive\Desktop\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 3 items                                                                                                                                               

tests\test_game_logic.py ...                                                                                                                              [100%]

====================================================================== 3 passed in 0.47s =======================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

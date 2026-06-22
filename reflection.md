# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  Ans: Game looked normal when i ran it for the first time.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  Ans: 
  1. Yes the hints were backwards. It was giving go lower for the number that was higher and "Go higher" for the number that was smaller.
  2. for the first game when I submitted the correct guess, it showed "you won message" but when I clicked new game it showed showed the message that you already won, start new game. Even when I was submitting my guess for next game it was showing that same mesasge.
  3. for the same input, it gives completely opposite hint.
  4. After loosing a game and selecting new game message still tells that you lost the game, start new game.
  5. Input bar says "Press enter to apply" but doesnt apply on pressing enter.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|   50  | Hint: Go Higher!  | Hint: Go Lower  |         None           |
|   70  | Hint: Go Lower    | Hint: Go Higher!|         None           |
|   57  | Final Score:90    | Final Score: 40 |         None           |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Ans:I used Claude Code during this project to help identify bugs, understand the codebase, and explain the error.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Ans:Claude identified that the hint logic in logic_utils.py was inverted. When the guess was too high, the game showed "Go HIGHER", and when the guess was too low, it showed "Go LOWER". Claude suggested to change the messages to fix it. This suggestion was correct. I verified it by running the game and testing guesses above and below the secret number. After the fix, the game was showing correct hints.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Ans:
Claude suggested that adding an empty conftest.py file would fix a pytest import error- ModuleNotFoundError: No module named 'logic_utils'. It solved the issue but I learned that the root cause was about Python's import path configuration rather than the game logic itself. I verified this by testing imports and reviewing the project structure. This suggestion was somewhat misleading because it treated the symptom rather than explaining the underlying cause.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Ans:
I decided a bug was fixed by reproducing the issue before the change and then testing the same scenario after applying the fix. If the game behaved as expected and no new issues appeared, I considered the bug fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Ans:
  One test I ran was checking the higher/lower hint logic. I entered guesses that were above and below the secret number and verified that the game displayed the correct hints ("Go LOWER" for high guesses and "Go HIGHER" for low guesses). This showed that the hint logic was working correctly after the fix.

  I also ran the pytest test suite after making changes. The tests passed successfully, which gave me confidence that the game logic was working as expected and that my fixes did not break existing functionality.

- Did AI help you design or understand any tests? How?
  Ans:
  AI helped me understand the existing tests and suggested additional scenarios to check, such as validating hint messages, score calculations, and new game behavior. This helped me verify that the fixes worked correctly.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Ans:
Streamlit reruns the entire script every time a user interacts with the app. Session state acts like memory and stores values such as the secret number, score, and attempts so they are not lost during those reruns. Without session state, the game would restart after every interaction.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Ans:
  One habit I want to reuse is testing each fix immediately after making a change instead of waiting until the end. This helped me catch issues quickly and verify that the bug was actually fixed.

- What is one thing you would do differently next time you work with AI on a coding task?
Ans:
Next time I will use different sessions for each bug and try to understand the flow of code first. That will help me find problems in code early and quickly.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
Ans:
This project taught me that AI-generated code can be very helpful for debugging and finding issues, but its suggestions should always be tested and verified. AI is a useful teammate, but not a replacement for understanding the code myself.

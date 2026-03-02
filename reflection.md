# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  I see the difficulty level settings, easy has 5 attempts, normal has 7 and difficult has 4, which is a little weird? since you would expect the easy mode to have more attempts than the normal level. nevermind it's the 1-20 that's not changing for easy mode
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. When I gave a guess that was lower than the actual number, it gave me a hint saying "Go lower" which is the opposite of what it should have said ("Go higher")
  2. When clicking new game, it should clear the current guess inside the textbox? but it doesn't so my guess from before is still there. the "You already won. Start a new game to play again." message also persists, when it should already be gone after I clicked start new game. And then when i try to play a new game, no hints are given anymore. The game just doesn't work anymore
  3. Easy mode says 1-20 but it actually is still between 1-100

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used GitHub Copilot inside VS Code to analyze the existing codebase and explain parts of the logic I didn’t immediately understand. I mainly used it     through inline chat and by referencing specific files to get context-aware explanations. I also used it to refactor my code and update the code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  Copilot pointed out that the “New Game” button wasn’t properly resetting the game state because the reset logic was placed after other conditions in the
  script. It suggested reordering the code so the session state updates happened earlier. After moving that logic, clicking “New Game” correctly reset the
  secret number and cleared previous messages. I verified the fix by finishing a game and starting multiple new rounds to confirm everything refreshed
  properly.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  At one point, Copilot suggested restructuring a larger portion of the game logic to fix the incorrect hint messages. However, after reviewing the code
  more carefully, I realized the real issue was just a reversed conditional statement. I verified this by simply swapping the comparison logic, which
  immediately fixed the hints without needing a major refactor.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I considered a bug fixed only if I could reproduce the original issue and then confirm it no longer happened under the same conditions. I tested
  multiple scenarios instead of just one successful run. If the behavior stayed consistent across several attempts, I felt confident the fix worked.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

  After fixing the hint logic, I manually guessed numbers both higher and lower than the secret number to verify the messages were correct in each case.
  This showed me that the conditional logic was now working properly in both directions. I also tested starting a new game multiple times to ensure the
  state fully reset.
- Did AI help you design or understand any tests? How?

  AI helped by suggesting edge cases to think about, such as what happens after winning and immediately clicking “New Game.” It encouraged me to test
  repeated interactions instead of just a single playthrough. That made my testing more thorough and intentional.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  The secret number kept changing because Streamlit reruns the entire script every time the user interacts with the app. Since the number wasn’t stored in
  session state, it was being regenerated on each rerun.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  I would explain that Streamlit reruns the whole program whenever you click a button or change input. If you don’t store important variables in
  st.session_state, they reset each time. Session state acts like memory that survives those reruns.
- What change did you make that finally gave the game a stable secret number?

  I initialized the secret number inside st.session_state and only generated it if it didn’t already exist. This ensured the number stayed consistent
  across guesses and interactions.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  
    I want to continue using clear `# FIX ME` comments to organize what needs to be addressed. Writing reflections alongside fixes also helped me think
    more intentionally about my debugging process.
- What is one thing you would do differently next time you work with AI on a coding task?

  Next time, I would spend more time reasoning through the bug myself before asking AI for a solution. I realized that understanding the problem first
  makes AI suggestions more useful and easier to evaluate.
- In one or two sentences, describe how this project changed the way you think about AI generated code.

  This project showed me that AI-generated code is a starting point, not a finished solution. It can accelerate debugging, but it still requires careful
  human judgment and testing.

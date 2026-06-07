# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game loaded with difficulty settings — easy (5 attempts, 1–20), normal (7 attempts, 1–100), and hard (4 attempts, 1–100). At first glance the attempt counts looked odd since easy had fewer attempts than normal, but the bigger issue was that the easy mode range was not actually being applied: the secret number was still being picked from 1–100 regardless of the setting. The game was technically playable but broken in several ways beneath the surface.

- List at least two concrete bugs you noticed at the start:
  1. The hints were backwards — when my guess was lower than the secret number, the game said "Go lower" instead of "Go higher." This made the game impossible to play correctly since every hint sent you in the wrong direction.
  2. Clicking "New Game" did not properly reset the game state. My previous guess stayed in the text box, the "You already won" message persisted on screen, and when I tried to play again no hints appeared at all — the game was stuck in a broken post-win state.
  3. Easy mode displayed "1–20" but the secret number was still randomly chosen from the full 1–100 range, meaning the stated range was misleading.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude Chat and Claude Code throughout this project — Claude Chat for explaining concepts and talking through bugs, and Claude Code directly in the editor for reading and editing the source files.


  I used GitHub Copilot inside VS Code to analyze the existing codebase and explain parts of the logic I didn’t immediately understand. I mainly used it     through inline chat and by referencing specific files to get context-aware explanations. I also used it to refactor my code and update the code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  When I described the hint bug, Claude immediately identified that the comparison operators in the hint logic were flipped — the code was using `>` where it should have used `<` and vice versa. I verified the fix by running the game and deliberately guessing numbers I knew were too low or too high, confirming that the hints now correctly said "Go higher" and "Go lower" in the right situations.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Claude was generally helpful, but at one point when I described the new-game reset issue, it initially gave a partial fix that cleared the text box but did not reset the session state variables tracking game progress. I verified it was incomplete by clicking "New Game" after a win and finding the game still refused to accept guesses. I had to give Claude more specific context about which state variables existed before it produced a complete fix.

  At one point, Copilot suggested restructuring a larger portion of the game logic to fix the incorrect hint messages. However, after reviewing the code
  more carefully, I realized the real issue was just a reversed conditional statement. I verified this by simply swapping the comparison logic, which
  immediately fixed the hints without needing a major refactor.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I only considered a bug fixed when I could reproduce the original problem and confirm it no longer happened. For example, to verify the hint fix I intentionally guessed a number I knew was wrong and checked that the direction made sense. If the behavior matched what a correct game should do, I considered it fixed.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  I ran the existing pytest suite after each fix to catch regressions, and also manually tested the game by playing through full rounds on each difficulty. The manual tests were especially useful for catching the new-game reset bug because the broken state only appeared after completing a game — pytest alone would not have surfaced that sequence.

- Did AI help you design or understand any tests? How?
  Yes — Claude helped me think through edge cases for the hint logic by asking me to consider what should happen when the guess equals the secret number, when it is too low, and when it is too high. That framing helped me structure my manual tests around those three cases rather than just clicking around randomly.

  AI helped by suggesting edge cases to think about, such as what happens after winning and immediately clicking “New Game.” It encouraged me to test
  repeated interactions instead of just a single playthrough. That made my testing more thorough and intentional.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  In the original code, the secret number was generated with `random.randint()` at the top level of the script, outside of any state management. Every time the player made a guess, Streamlit reran the entire script from top to bottom, which called `random.randint()` again and picked a brand new number. So you were never actually guessing the same target twice.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  I would explain that Streamlit reruns the whole program whenever you click a button or change input. If you don’t store important variables in
  st.session_state, they reset each time. Session state acts like memory that survives those reruns.
  Imagine every time you click a button in the app, Python reruns your entire script from scratch — like refreshing a page that forgets everything. Session state is like a sticky notepad that survives those reruns. Anything you store in `st.session_state` stays put between reruns, so the secret number only gets generated once and sticks around for the whole game.

- What change did you make that finally gave the game a stable secret number?
  I wrapped the secret number generation in a check: if the key did not already exist in `st.session_state`, generate a new number and store it there; otherwise leave it alone. That way the number is only picked once per game, and every guess within that game is checked against the same target.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  
    I want to continue using clear `# FIX ME` comments to organize what needs to be addressed. Writing reflections alongside fixes also helped me think
    more intentionally about my debugging process.
  Giving AI specific context — the actual code snippet, the exact error or wrong behavior, and what I expected instead — got me far better answers than vague descriptions. I want to keep that habit of being precise with my prompts rather than just saying "this is broken, fix it."

- What is one thing you would do differently next time you work with AI on a coding task?

  Next time, I would spend more time reasoning through the bug myself before asking AI for a solution. I realized that understanding the problem first
  makes AI suggestions more useful and easier to evaluate.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  AI-generated code is a strong first draft, not a finished answer — it can get the logic directionally right but still miss edge cases or leave state variables in an inconsistent state. I now treat AI suggestions as something to test and read critically rather than something to paste in and trust.

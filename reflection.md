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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

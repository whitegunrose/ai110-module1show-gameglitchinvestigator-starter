# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

> I noticed that the `new game` button did not work. Every time I ran out of attempts and
tried to start a new game with the button, it was never able to start a new game. I had
to go and manually refresh the page each time.

> It seems that the button would only work for me if I clicked it in the middle of a current game. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  399  |     Go LOWER!     |    Go HIGHER!   |   None (logic error)   |
| -10000|    Go HIGHER!     |     Go LOWER!   |   None (logic error)   |
|  101  |     Go LOWER!     |    Go HIGHER!   |   None (logic error)   |
| Easy  |    Range 1-20     |   Range 1-100   |   Improper difficulty range   |
| Easy  |  6 max attempts   |   5 attempts    |   Improper difficulty attempts   |
|Normal |    Range 1-20     |   Range 1-50    |   Improper difficulty range   |
|Normal |  8 max attempts   |   7 attempts    |   Improper difficulty attempts   |
| Hard  |  5 max attempts   |   4 attempts    |   Improper difficulty attempts   |


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

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

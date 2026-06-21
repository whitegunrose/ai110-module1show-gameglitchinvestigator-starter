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

> I strictly used Claude COde for this project. One example of an AI suggestion that was correct was to properly implement functions in `logic_utils.py`. The lack of implementations were pointed out to me once I had asked Claude to write tests for all of the bugs listed in the `Bug Reproduction Log` above. One example of an incorrect or misleading suggestion that Claude made was the improper handling of PATH commands on to run the pytests.

> All of these changes and corrections were verified by ensuring the passing of all tests in `tests/test_game_logic.py`
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

> I decided that a bug was really fixed when the tests for that bug ran.
> One test I ran with pytest was fixing the bounds for the input of `399`
- AI helped me design and understand the tests based off of the bugs I logged in the `Bug Reproduction Log`
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

> Streamlit "reruns" and handles session state by keeping track of the current state of the game with a string variable. The values were `Win`, `Too High` or `Too Low`. The game keeps going as long as the state is not `Win`. The `new game` button will refresh the state of the game to a value other than `Win` and reset the amount of remaining attempts`.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

> One habit or strategy I want to reuse in future labs and projects is to keep a `Bug Reproduction Log` that would be easy for AI to parse and understand. One thing I would do differently is work very incrementally with each bug and break it down into more bite sized tasks to digest the work easier. This project changed the way I think about AI generated code in how I view its authenticity. As long as we as developers are properly reviewing the code the AI is changing and truly understand why it is doing what it is, there is no problem with using AI.
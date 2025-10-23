# 🪨📜✂️ Rock Paper Scissors – Python Console Game

A simple, fun, and fully interactive **Rock Paper Scissors**  single player game built with Python!  
Play against the computer, keep score across multiple rounds, and quit anytime.  
Designed with input validation, clean user feedback, and emoji-based visuals 🎮

---

## 🎯 Features

- ✅ Interactive console gameplay  
- ✅ Emoji representation for moves  
- ✅ Input validation (only `r`, `p`, `s`, or `q` accepted)  
- ✅ Custom number of rounds  
- ✅ Option to quit mid-game  
- ✅ Auto-calculated wins, losses, and ties  
- ✅ Option to replay or exit after finishing  

---

## 🧠 Game Rules

- **r → Rock 🪨**  
- **p → Paper 📜**  
- **s → Scissors ✂️**

🪨 beats ✂️  
📜 beats 🪨  
✂️ beats 📜  

Tied if both choose the same move.

---

## 🚀 How to Play

1. **Run the script:**
   ```bash
   python rock_paper_scissors.py
   ```
2. Enter `y` to start the game.
3. Choose the number of rounds to play.
4. In each round, type:
   - `r` → Rock  
   - `p` → Paper  
   - `s` → Scissors  
   - `q` → Quit anytime
5. After all rounds (or if you quit), the game shows:
   - Total rounds played  
   - Number of wins, losses, and ties  
   - Final scores and winner declaration
6. Choose whether to play again or exit.

---

## 🧩 Code Structure

| Function | Description |
|-----------|--------------|
| `play_round(rounds)` | Handles all gameplay logic for the given number of rounds. |
| `game_start()` | Initializes the game, manages replay logic, and shows results. |
| `game_end()` | Displays a thank-you message and exits the program. |

---

## 🧱 Built With
- 🐍 **Python 3**
- 📦 `random` module (for computer moves)

---

## 📸 Sample Gameplay

```
Welcome to Rock Paper Scissors!
========================================
Start the game? (y/n): y
How many rounds do want to play?: 3

--------------------
Round-1:
--------------------
Rock! Paper! Scissors? (r/p/s) or q to quit: r
You chose: 🪨
Computer Chose: ✂️
You Won!
...
```

---

## 🏁 Author

**Shafin Ahmed**  
🎓 Computer Science & Engineering Student | BRAC University 

---

## 🧾 License
This project is open-source.

---

**⭐ If you like this project, give it a star on GitHub!**

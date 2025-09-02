# 🏓 Shapes Paddle Game

## 📖 About the Game
This is a **two-player paddle game** built with Python and the `turtle` module.  
Players control paddles and try to **catch falling shapes** to score points.  
The first player to reach **100 points** wins the game!

---

## 📂 Project Files
- `start_game_cubes.py` → Main file to run the game
- `body_paddle.py` → Paddle class
- `shapes.py` → Shapes and their logic
- `score_shapes.py` → Scoreboard logic

---

## 🖼 Game Screenshot
<img width="1200" height="629" alt="image" src="https://github.com/user-attachments/assets/9c4703dd-b189-4199-a993-1b644dbd883b" />


---

## 🎮 Controls
### Player 1 (Right Side):
- `→` Move Right
- `←` Move Left

### Player 2 (Left Side):
- `D` Move Right
- `A` Move Left

---

## 🏆 Rules to Win or Lose
✔ **Win:** First player to reach **100 points**.  
✖ **Lose:** If you miss too many shapes (tries decrease).  
🐢 **Special Case:** If you catch the **white turtle**, the game ends immediately and determines the winner.  

---

## ⚙️ Requirements
- **Python 3.8+**
- `turtle` module (usually comes with Python)

---

## ▶️ How to Run
1. Make sure all files are in the same folder:
   - `start_game_cubes.py`
   - `body_paddle.py`
   - `shapes.py`
   - `score_shapes.py`
2. Run the game using:
```bash
python start_game_cubes.py

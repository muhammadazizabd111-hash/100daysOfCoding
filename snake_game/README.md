# Classic Snake Game 🐍

A polished implementation of the classic Snake game built in Python using the `turtle` graphics module. Guide the snake to eat food, grow longer, and achieve a high score without hitting the walls or your own tail!

---

## Features ✨
* **Smooth Movement & Grid System:** Classic arcade-style snake mechanics.
* **Dynamic Scoring:** Score updates instantly every time the snake eats food.
* **Collision Detection:** 
  * Wall collision detection (ends the game if you hit the boundaries).
  * Self-collision detection (ends the game if the snake bites its own tail).
* **Rapid-Turn Bug Prevention:** Includes a custom frame-lock mechanism (`turned_this_frame`) to prevent accidental 180-degree self-collisions caused by fast double-keystrokes.

---

## Project Structure 📁
* `main.py` — The core game loop, screen setup, and collision listeners.
* `snake.py` — Controls the snake's body parts, movement logic, and steering rules.
* `food.py` — Generates and randomly repositions food items.
* `scoreboard.py` — Handles score tracking and the "Game Over" display.

---

## Requirements 🛠️
* Python 3.x
* Built-in `turtle` library (comes pre-installed with standard Python installations).

---

## How to Run 🚀

1. Clone or download this repository.
2. Open your terminal or command prompt in the project directory.
3. Run the game using Python:
   ```bash
   python main.py
   ```

---

## Controls 🎮
* **Up Arrow** — Move Up
* **Down Arrow** — Move Down
* **Left Arrow** — Move Left
* **Right Arrow** — Move Right

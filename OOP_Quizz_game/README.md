# Python Trivia Quiz Game

A simple command-line trivia game built in Python that tests your general knowledge with True/False questions and keeps track of your score.

---

## Features

* **Dynamic Question Bank:** Loads trivia questions and answers cleanly from a data model.
* **Interactive Gameplay:** Prompts users step-by-step through each question.
* **Score Tracking:** Tracks correct answers in real-time and displays a final score upon completion.
* **Case-Insensitive Input:** Accepts various capitalizations (e.g., `true`, `True`, `TRUE`).

---

## Project Structure

```text
├── main.py           # Application entry point; drives the game loop
├── question_model.py # Defines the Question class
├── quiz_brain.py     # Manages game logic, scoring, and user flow
└── data.py           # Contains the dataset of trivia questions and answers

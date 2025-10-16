

# World of Games (WoG)

## Overview

**World of Games (WoG)** is a Python-based game collection that allows players to choose from **three different games** and test their skills. After each game, a **score** is calculated based on performance and difficulty.

The project also includes an automated **score testing service** (`test_scores_service`) to ensure the score displayed is valid.

Additionally, WoG can be run as a **web application using Flask**, allowing players to interact with the games through a browser.

---

## Features

* **Three Game Types**:

  1. **Memory Game** – A sequence of numbers appears for 1 second; the player must recall it correctly.
  2. **Guess Game** – The player guesses a number and tries to match the computer’s choice.
  3. **Currency Roulette** – The player guesses the value of a random amount of USD in ILS.

* **Difficulty Levels**: Players can choose a difficulty from 1 to 5, affecting the challenge and scoring.

* **Score System**: Scores are calculated and stored after each successful game.

* **Automated Score Test**: `test_scores_service` validates that the score element on the web page is a number between 1 and 1000.

* **Web Integration**: Can run as a Flask web app with dynamic score display and game selection.

---

## How to Play

### CLI Version

1. Run the main launcher:

```bash
python main.py
```

2. **Welcome Message**:

```text
Hello <name> and welcome to the World of Games (WoG).
Here you can find many cool games to play.
```

3. **Choose a Game**:
   Enter a number from 1 to 3:

   * `1` – Memory Game
   * `2` – Guess Game
   * `3` – Currency Roulette

4. **Choose Difficulty**:
   Enter a difficulty level from 1 to 5.

5. **Play the Game**:
   The game runs according to the selected type and difficulty.

6. **Score**:
   If the player succeeds, the score is calculated and stored using `add_score()`.

---

### Flask Web Version

1. Install Flask and dependencies (see below).
2. Run the Flask server:

```bash
python app.py
```

3. Open a browser at `http://127.0.0.1:5000/` to play the games.
4. Scores are displayed dynamically on the page.

---

## Automated Score Testing

The `test_scores_service.py` file verifies that the score displayed on the web page is valid:

1. Takes the application URL as input.
2. Opens a headless browser using Selenium.
3. Locates the score element by its ID (`id="score"`).
4. Validates that the score is a number between 1 and 1000.
5. Returns `True` if valid, `False` otherwise.

---

## Installation

### Python Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### `requirements.txt` Example

```
Flask
requests>=2.31.0
freecurrencyapi
numpy>=1.25.0
selenium
```

> Make sure **Chrome** is installed and ChromeDriver is set up for the automated testing service.

---

## Project Structure

```
WoG/
│
├── MainGame.py              # Game launcher
├── GuessGame.py             # Guess Game logic
├── MemoryGame.py            # Memory Game logic
├── CurrencyRouletteGame.py  # Currency Roulette logic
├── Score.py                 # Score management
├── test_scores_service.py   # Automated score testing
├── app.py                   # Flask web app
├── requirements.txt         # Project dependencies
└── README.md
```

---

## Notes

* Modular design allows easy addition of new games or difficulty levels.
* Can be extended to **store high scores**, integrate with **more APIs**, or create advanced UI.
* Uses **Flask, NumPy, and FreeCurrencyAPI** for web interaction, random generation, and currency conversions.
* Encourages **Python best practices**, including input validation, modular coding, and automated testing.

---

If you want, I can **also write a polished `requirements.txt`** and a **ready-to-use `app.py` Flask file** to make this project fully web-enabled.

Do you want me to do that next?

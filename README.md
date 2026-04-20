# Python Decision Logic: Stone-Paper-Scissors

## Overview
This project is a terminal-based implementation of "Stone, Paper, Scissors." It focuses on utilizing Python functions and conditional logic gates to simulate a competitive environment between a user and the system. 

## Technical Stack
- **Language:** Python 3.x
- **Core Concepts:**
    - Function Definition and Modular Programming
    - List Management and Random Selection (`random.choice`)
    - String Normalization (`capitalize()`)
    - Complex Boolean Logic (Compound Conditionals)

## Key Features
* **Modular Design:** The core game logic is encapsulated within a defined function for reusability.
* **User Experience:** Implements string normalization to ensure that inputs like "stone," "STONE," or "StOnE" are all processed correctly as "Stone."
* **Robust Logic:** Uses compound `if` statements to efficiently check for winning conditions, reducing the need for deeply nested loops.
* **Input Protection:** Verifies that the user's choice exists within the pre-defined game set before executing the decision logic.

## How To Run
1. Clone the repository.
2. Navigate to the project directory.
3. Run the game:
   ```bash
   python stone_paper_scissors.py

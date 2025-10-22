# Sudoku

A desktop Sudoku game built with Python and [Pygame](https://www.pygame.org/). The project provides randomly generated Sudoku puzzles across multiple difficulties and an interactive interface for solving them.

## Features

- **Multiple difficulties** – choose between Easy, Medium, or Hard puzzles from the start screen.
- **Random puzzle generation** – puzzles are generated on the fly using a custom Sudoku generator.
- **Interactive gameplay** – select cells with the mouse and enter numbers via the keyboard.
- **Quality-of-life controls** – reset the puzzle to its starting state, restart with a new board, or exit at any time.
- **Win/Loss feedback** – receive feedback when the board is completed and validated.

## Requirements

- Python 3.9+
- `pygame` 2.0+

Install the dependency with pip:

```bash
pip install pygame
```

## Running the game

From the repository root run:

```bash
python sudoku.py
```

A window will open prompting you to pick a difficulty. Use the mouse to select cells and the number keys (`1`-`9`) to fill them in. Press `Backspace` to clear a cell.

### Controls

| Action | Input |
| --- | --- |
| Select cell | Left-click |
| Place number | Number keys `1`-`9` |
| Clear selected cell | `Backspace` |
| Reset puzzle to original state | Click **Reset** |
| Restart with a new puzzle | Click **Restart** |
| Exit the game | Click **Exit** or close the window |

## Project structure

```
.
├── README.md              # Project documentation
├── sudoku.py              # Game loop and UI logic built with Pygame
└── sudoku_generator.py    # Sudoku puzzle generator and board utilities
```

## Troubleshooting

- **Pygame fails to initialize** – ensure the SDL dependencies for your platform are installed. On Linux you may need `sudo apt-get install python3-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev`.
- **Window is unresponsive** – confirm the game is running in a local environment with graphical support; headless servers typically cannot display the Pygame window.

Enjoy solving Sudoku!

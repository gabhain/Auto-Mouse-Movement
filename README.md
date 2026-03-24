# Auto Mouse Movement

A Python script that moves the mouse in random patterns to simulate activity.

## Features

- Randomized mouse movements (X and Y offsets)
- Returns to the original starting position after each pattern
- Configurable pattern size, steps, and duration
- Repeatable patterns with pauses in between

## Prerequisites

- Python 3.x
- `pyautogui` library

Install dependencies:

```bash
pip install pyautogui
```

## Usage

1. Run the script:
   ```bash
   python patterns.py
   ```
2. You will have 3 seconds to move your mouse to the desired starting position.
3. The script will execute the randomized movement and return to the start.

## Configuration

You can adjust the following parameters in `patterns.py`:

- `total_distance`: Overall size of the pattern.
- `steps`: Number of small random moves per pattern.
- `duration_per_step`: Speed of each small move.
- `repeat_count`: Number of times to run the pattern.

## License

MIT

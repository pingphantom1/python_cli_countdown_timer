# Python Countdown Timer

A simple command-line countdown timer built with Python. The program allows users to specify a countdown duration in hours, minutes, and seconds, displays the remaining time in real time, and provides the ability to pause and resume the countdown by pressing the **P** key.

## Features

- **Custom Countdown Duration:** Users can set their preferred countdown duration using the `HHMMSS` format.
- **Input Validation:** Ensures that the user enters exactly six digits and that the hours, minutes, and seconds are within the accepted ranges.
- **Real-Time Countdown:** Displays the remaining time in `HH:MM:SS` format.
- **Pause and Resume:** Press the **P** key to pause the countdown and press it again to resume.
- **Automatic Completion:** Displays a completion message when the countdown reaches zero.
- **Terminal Restoration:** Restores the terminal's original settings after the countdown finishes, including when an error occurs.

## Technologies Used

- **Python 3**
- `time` – Handles countdown timing.
- `sys` – Handles standard input and output operations.
- `tty` – Configures the terminal to capture individual keypresses.
- `termios` – Retrieves and restores terminal settings.
- `select` – Checks for keyboard input without blocking program execution.

## Requirements

- Python 3 installed on your computer.
- A Unix-like operating system (Linux or macOS) with terminal support for `tty` and `termios`.

**Note:** This program uses terminal-specific modules (`tty` and `termios`) and is not directly compatible with standard Windows Command Prompt or PowerShell.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate into the project directory:

   ```bash
   cd <project-directory>
   ```

3. Run the Python script:

   ```bash
   python3 countdown.py
   ```

   Replace `countdown.py` with the actual name of your Python file if it is different.

## How to Use

1. Run the program.
2. Enter the countdown duration in the requested `HHMMSS` format.
3. The countdown begins immediately after valid input is provided.
4. Press **P** to pause the countdown.
5. Press **P** again to resume the countdown.
6. Wait for the countdown to reach zero.

### Example

```text
Enter the duration before countdown begins in the format HHMMSS (e.g. 013045): 000130

Countdown for 0h 1m 30s...
Press P to pause/resume

Time left: 00:01:30
Time left: 00:01:29
Time left: 00:01:28

Paused. Press P to resume.

Resumed.

Time left: 00:00:45
Time left: 00:00:44

Countdown complete!
```

## Input Format

The countdown duration must be entered using six digits in the following format:

| Component | Description | Accepted Range |
|---|---|---|
| HH | Hours | 00–23 |
| MM | Minutes | 00–60 (as currently implemented) |
| SS | Seconds | 00–60 (as currently implemented) |

For example:

- `010000` – 1 hour.
- `003000` – 30 minutes.
- `000045` – 45 seconds.
- `013045` – 1 hour, 30 minutes, and 45 seconds.

## Project Structure

```text
project-directory/
│
├── countdown.py
├── README.md
└── .gitignore
```

## Learning Objectives

This project demonstrates practical applications of several Python programming concepts:

- Functions and return values.
- Loops and conditional statements.
- Exception handling.
- User input validation.
- Time calculations and countdown logic.
- Working with terminal input and output.
- Non-blocking keyboard input.
- Managing terminal settings.
- Using Git and GitHub for version control and collaborative development.

## Future Improvements

Possible enhancements include:

- Adding support for Windows terminals.
- Allowing users to stop or reset the countdown.
- Improving the input validation for minutes and seconds.
- Adding an audible notification when the countdown finishes.
- Supporting multiple countdown sessions.

## Author

Developed as a Python command-line programming project.

## License

This project is open-source and available for learning and educational purposes.
Internet Speed Test Application

A simple Python application that measures your internet speed (download, upload, and ping) using the `speedtest` library, with a user-friendly GUI built using `tkinter`.

Features

- Run internet speed test on your computer.
- Displays Download Speed, Upload Speed (in Mbps), and Ping (in ms).
- Simple graphical interface with a button to start the test.
- Modular code separating backend speed test logic and frontend GUI.

Requirements

- Python 3.x
- `speedtest-cli` Python package (install with `pip install speedtest-cli`)
- `tkinter` (usually included with Python)

Installation & Usage

1. Clone or download this repository.
2. Install the dependency:
`pip install speedtest-cli`
3. Run the GUI application:
`python gui\_main.py`
4. Click the "Run Speed Test" button to start.

Project Structure

- `speed_test.py` — Contains the speed test logic.
- `gui_main.py` — Contains the tkinter GUI code.


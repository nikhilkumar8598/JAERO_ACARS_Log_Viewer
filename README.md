
# JAERO ACARS Log Viewer

The **JAERO ACARS Log Viewer** is a web-based application designed to parse and display ACARS (Aircraft Communications Addressing and Reporting System) logs in real-time from JAERO. This app dynamically updates log entries and provides a convenient search feature for filtering log data. A server status indicator is also included to reflect the application's health.

---

## Features

- **Real-Time Log Viewer**: Automatically refreshes every 30 seconds to display the latest log entries.
- **Search Functionality**: Filter log entries by keyword in real-time.
- **Dynamic Server Status**: Displays a green or red dot at the top-right corner to indicate server status.
- **Responsive Design**: Optimized for both desktop and mobile viewing.
- **External Log Support**: Processes the latest ACARS log file in the current directory.

---

## Requirements

- Python 3.7 or later.
- Flask, collections, html, glob, logging.
- Basic knowledge of running Python applications.
- JAERO: https://github.com/jontio/JAERO with logging enabled.
---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/nikhilkumar8598/JAERO_ACARS_LogViewer.git
    cd JAERO_ACARS_LogViewer
    ```

2. Install dependencies:
    ```bash
    pip install flask
    ```

3. Ensure that ACARS log files are in the same directory as the app, following the format:  
    `acars-log-YY-MM-DD.txt`.

---

## Usage

1. Run the Flask application with the py file in the folder with the JAERO acars log file:
    ```bash
    python jaero_acars_viewer.py
    ```
	Or run using jaero_acars_viewer.exe.

2. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

3. The application will display the latest 500 log entries and update every 30 seconds.

---

## Log File Requirements

- Log files must be named in the format: `acars-log-YY-MM-DD.txt`.
- Place log files in the same directory as the application.
- Only the latest log file (based on modification time) is processed.

---

## Server Status Indicator

- A **green dot** at the top-right indicates the server is running correctly.
- A **red dot** indicates a server issue.

---

## Configuration

You can adjust the refresh interval and server status check frequency by modifying the JavaScript in `index.html`:

- **Log refresh interval**: Change the `setInterval(refreshPage, 30000)` value.

---

## File Structure

```
├── jaero_acars_viewer.py                # Main application file
├── templates/
│   └── index.html        # HTML file for rendering the log viewer
├── static/
│   └── styles.css        # CSS file for styling
├── README.md             # Project documentation
└── acars-log-YY-MM-DD.txt  # Example log files (not included)
```

---

## Example Logs

Example log entries should follow this pattern:

```
14:32:15 01-01-25 UTC    AES:123456 GES:7890 2 N12345 ! Airline Code Aircraft Info
    Message contents go here...
```

- Timestamps, registration, aircraft, airline and message content are dynamically parsed.

---

## Troubleshooting

1. **No log file found**: Ensure a file matching the pattern `acars-log-*.txt` exists in the current directory.
2. **Incorrect log format**: Verify the logs match the expected structure described above.
3. **Styling issues**: Clear your browser cache to apply the latest CSS changes.

---

## License

This project is open-source and distributed under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for improvements or bug fixes.


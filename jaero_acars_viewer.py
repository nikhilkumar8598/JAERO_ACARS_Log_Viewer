import os
import re
from flask import Flask, render_template, jsonify
from collections import deque
import html
import glob
import logging,sys

app = Flask(__name__)

def find_latest_log_file():
    """
    Finds the most recently modified log file in the current directory
    that matches the pattern "acars-log-*.txt".
    
    Returns:
        str: The path to the most recent log file, or None if no file is found.
    """
    log_pattern = "acars-log-*.txt"  # Pattern to match log files in the current directory
    log_files = glob.glob(log_pattern)  # Get all log files matching the pattern
    
    if not log_files:
        return None  # No files found
    
    # Find the most recently modified log file
    latest_log_file = max(log_files, key=os.path.getmtime)
    return latest_log_file

def process_log_file(file_path):
    """
    Processes the log file to extract the most recent 500 entries.

    Args:
        file_path (str): Path to the log file.

    Returns:
        list: List of the most recent 500 parsed log entries.
    """
    if not file_path:
        logging.error("No log file with name acars-log-*.txt found.")
        return {"error": "No log file with name acars-log-*.txt found."}
    
    pattern = re.compile(
        r"(?P<timestamp>\d+:\d+:\d+ \d{2}-\d{2}-\d{2} UTC)\s+AES:[A-F0-9]+\s+GES:\d+\s+2\s+(?P<registration>.+?)\s+!\s+[A-Z0-9]{2}\s+[A-Z]\s+(?P<aircraft_and_airline>.+?)\n(?P<message>(?:\s+(?!\d+:\d+:\d+ \d{2}-\d{2}-\d{2} UTC).+?\n)+)",
        re.IGNORECASE,
    )

    entries = deque(maxlen=500)  # Store up to 500 entries

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            log_data = file.read()
            matches = pattern.finditer(log_data)
            for match in matches:
                if "JAERO" in match.group(0):
                    continue
                timestamp = match.group("timestamp")
                registration = re.sub(r"[^A-Za-z0-9\-]", "", match.group("registration"))
                aircraft_and_airline = match.group("aircraft_and_airline").strip()
                message = match.group("message").strip()

                # Escape special HTML characters in the message for safe rendering
                escaped_message = html.escape(message)

                entries.append({
                    "timestamp": timestamp,
                    "registration": registration,
                    "aircraft_and_airline": aircraft_and_airline,
                    "message": escaped_message,  # Escaped message for HTML
                })
    return list(reversed(entries))  # Most recent entries appear on top


@app.route("/")
def index():
    entries = process_log_file(find_latest_log_file())
    return render_template("index.html", entries=entries)


@app.route("/api/entries")
def api_entries():
    entries = process_log_file(find_latest_log_file())
    return jsonify(entries)


if __name__ == "__main__":
    app.run(debug=True)

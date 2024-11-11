# RDP Data Simplification Tool

This tool simplifies data by reducing the number of points in a curve using the Ramer-Douglas-Peucker (RDP) algorithm. Users can specify an epsilon value to control the level of simplification.

**Features:**

* Interactive plot visualization of original and simplified data.
* User-friendly interface for selecting an input CSV file and adjusting the epsilon value.
* Export functionality to save the simplified data as a new CSV file.

**Installation:**

1. Ensure you have Python 3 installed on your system. You can check by running `python3 --version` in your terminal.
2. Install the required libraries:

```bash
pip install tkinter pandas matplotlib rdp  # Replace 'rdp' with the library name if not built-in

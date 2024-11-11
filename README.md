# RDP Data Simplification Tool
# By Dario Di Nunzio
# https://www.linkedin.com/in/dariodinunzio/
# 2024-11-10

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

**Usage:**

1. Run the script using the command:
'''bash
python main.py

2. Click the "Select CSV File" button to choose your data file. The file must be a simple CSV with X-coordinates in the first column and Y-coordinates in the second column.
3. Adjust the epsilon slider to control the level of simplification. Higher epsilon values lead to greater reduction in points.
4. Click the "Plot" button to visualize the original and simplified data.
5. Click the "Export" button to save the simplified data to a new CSV file named simplified_data.csv.

**Example Usage:**

1. Download a sample CSV file containing X and Y coordinate data.
2. Run the script python main.py.
3. Select the sample CSV file using the "Select CSV File" button.
4. Adjust the epsilon slider and observe the corresponding changes in the plot.

**License:**

This project is licensed under the MIT License (see LICENSE file).

**Contact:**

Feel free to reach me out for any questions or feedback.

# Data Simplification Tool
# By Dario Di Nunzio
# https://www.linkedin.com/in/dariodinunzio/
# 2024-11-10
# This tool uses the Ramer-Douglas-Peucker Algorithm to reduce the number of points in a curve based on
# the parameter epsilon specified by the user.
# The input must be a simple CSV file with the X-coordinates on first column and Y-coordinates on second column.

import tkinter as tk
from tkinter import filedialog, messagebox
from rdp import rdp
import matplotlib.pyplot as plt
import pandas as pd


def plot_data(epsilon):
    # Clear the current plot
    plt.clf()
    try:
        x_coordinates = data[data.columns[0]].to_list()
        y_coordinates = data[data.columns[1]].to_list()
        input_coordinates = list(zip(x_coordinates, y_coordinates))

        # Simplify data with RDP algorithm
        output_coordinates = rdp(input_coordinates, epsilon)

        # Plot original data (blue)
        plt.plot(x_coordinates, y_coordinates, label='Original Data', color='blue')

        # Plot simplified data (red)
        plt.plot([p[0] for p in output_coordinates], [p[1] for p in output_coordinates], label='Simplified Data',
                 color='red')

        # Add labels and title
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Original vs. Simplified Data')

        # Add legend to differentiate lines
        plt.legend()

        plt.show()

    except NameError:
        messagebox.showinfo("Error", "No input file provided")


def export_data(epsilon):
    try:
        x_coordinates = data[data.columns[0]].to_list()
        y_coordinates = data[data.columns[1]].to_list()
        input_coordinates = list(zip(x_coordinates, y_coordinates))

        # Simplify data with RDP algorithm
        output_coordinates = rdp(input_coordinates, epsilon)

        # Create a DataFrame from the simplified data
        df = pd.DataFrame(output_coordinates, columns=['X', 'Y'])

        # Export the DataFrame to a CSV file
        df.to_csv('simplified_data.csv', index=False)
        messagebox.showinfo("Export Successful", "Data exported to simplified_data.csv")

    except NameError:
        messagebox.showinfo("Error", "No input file provided")


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        global data
        data = pd.read_csv(file_path)


root = tk.Tk()
root.title("RDP point reducer")
root.geometry("400x120")  # Adjust window size

epsilon_var = tk.DoubleVar(value=0.5)

slider = tk.Scale(root, from_=0.0, to=1.0, variable=epsilon_var, orient=tk.HORIZONTAL, resolution=0.1)
slider.grid(row=0, column=0, columnspan=2, sticky="ew")

plot_button = tk.Button(root, text="Plot", command=lambda: plot_data(epsilon_var.get()))
plot_button.grid(row=1, column=0, sticky="ew")

export_button = tk.Button(root, text="Export", command=lambda: export_data(epsilon_var.get()))
export_button.grid(row=1, column=1, sticky="ew")

select_file_button = tk.Button(root, text="Select CSV File", command=select_file)
select_file_button.grid(row=2, column=0, columnspan=2, sticky="ew")

root.grid_columnconfigure(0, weight=1)  # Expand column 0
root.grid_columnconfigure(1, weight=1)  # Expand column 1

root.mainloop()

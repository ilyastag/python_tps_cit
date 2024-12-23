# Create main window
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ComboBox Example")
root.geometry("300x200")

# Label to display selected value
label = tk.Label(root, text="Your selection will appear here")
label.pack(pady=10)

# List of options
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create a ComboBox
combo = ttk.Combobox(root, values=options, state="readonly")  # 'readonly' prevents manual input
combo.pack(pady=10)

# Set default value
combo.set("Select an option")  # Display this as the default text

# Function to get the selected value
def display_selection(event):
    selected_value = combo.get()
    label.config(text=f"You selected: {selected_value}")

# Bind the ComboBox selection event
combo.bind("<<ComboboxSelected>>", display_selection)

# Run the application
root.mainloop()
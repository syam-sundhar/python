import tkinter as tk
from tkinter import messagebox

def greet_user():
    """Triggers when the button is clicked, using the selected radio button value."""
    user_name = name_entry.get()
    
    # Retrieve the current value from the radio button variable
    chosen_color = color_var.get()
    
    if user_name.strip():
        # Update text and dynamically change color based on radio selection
        output_label.config(text=f"Hello, {user_name}! Dynamic GUI updated.", fg=chosen_color)
    else:
        messagebox.showwarning("Input Error", "Please enter your name first!")

# 1. Main window setup
root = tk.Tk()
root.title("GUI Radio Button Demo")
root.geometry("400x320")

# 2. Name entry widgets
instruction_label = tk.Label(root, text="Enter your name:", font=("Arial", 11))
instruction_label.pack(pady=5)

name_entry = tk.Entry(root, font=("Arial", 11), width=25)
name_entry.pack(pady=5)

# 3. Radio button setup
radio_frame = tk.LabelFrame(root, text=" Choose Text Color ", padx=10, pady=10)
radio_frame.pack(pady=15)

# Special Tkinter variable to track which radio button is active
color_var = tk.StringVar(value="blue") 

# Radio button choices mapping (Display Label -> Hex/Color Code)
colors = [("Blue Theme", "blue"), ("Green Theme", "green"), ("Red Theme", "red")]

for text, color_value in colors:
    # Each radio button shares the same 'variable' but has a unique 'value'
    rb = tk.Radiobutton(radio_frame, text=text, variable=color_var, value=color_value)
    rb.pack(anchor="w") # Align left (West)

# 4. Action button
submit_button = tk.Button(root, text="Apply & Greet", command=greet_user, bg="#000000", fg="white")
submit_button.pack(pady=10)

# 5. Output label
output_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
output_label.pack(pady=10)

root.mainloop()
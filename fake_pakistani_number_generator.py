import tkinter as tk
from tkinter import messagebox
import random

def generate_pakistani_number():
    # Pakistani numbers start with +92, followed by a 10-digit number starting with 3, 30-34
    country_code = "+92"
    first_digit = random.choice(["3"])
    second_part = random.choice([f"{i}" for i in range(0, 5)])  # 30-34
    rest_digits = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    phone_number = f"{country_code}{first_digit}{second_part}{rest_digits}"
    return phone_number

def generate_and_display():
    try:
        count = int(entry_count.get())
        if count <= 0 or count > 999:
            messagebox.showerror("Error", "Please enter a number between 1 and 999.")
            return
        text_output.delete(1.0, tk.END)
        for _ in range(count):
            number = generate_pakistani_number()
            text_output.insert(tk.END, f"{number}\n")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Pakistani Fake Number Generator")
root.geometry("400x500")

# Create and place widgets
label_instruction = tk.Label(root, text="Enter how many fake numbers to generate (1-999):")
label_instruction.pack(pady=10)

entry_count = tk.Entry(root)
entry_count.pack(pady=5)

button_generate = tk.Button(root, text="Generate Numbers", command=generate_and_display)
button_generate.pack(pady=10)

text_output = tk.Text(root, height=20, width=40)
text_output.pack(pady=10)

# Start the main loop
root.mainloop()
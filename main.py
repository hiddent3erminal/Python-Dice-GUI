import tkinter as tk
import random
import time

# Function to roll the dice and display the corresponding numbers with animation
def roll_dice():
    for _ in range(10):  # Loop to create rolling animation
        dice_number1 = random.randint(1, 6)
        dice_number2 = random.randint(1, 6) if roll_two.get() else None

        dice_label1.config(text=str(dice_number1), fg=dice_color.get())
        if dice_number2 is not None:
            dice_label2.config(text=str(dice_number2), fg=dice_color.get())
            dice_label2.pack(side="left", padx=20)
        else:
            dice_label2.pack_forget()

        window.update()  # Update the window to reflect the new dice number
        time.sleep(0.1)  # Pause briefly to simulate animation

# Create main window
window = tk.Tk()
window.title("Dice Roller App")
window.geometry("400x400")
window.configure(bg="lightblue")

# Title Label
title_label = tk.Label(window, text="Roll the Dice!", font=("Arial", 18), bg="lightblue")
title_label.pack(pady=10)

# Dice display (initially empty)
dice_frame = tk.Frame(window, bg="lightblue")
dice_frame.pack(pady=20)

dice_label1 = tk.Label(dice_frame, text="-", font=("Arial", 100), bg="lightblue")
dice_label1.pack(side="left", padx=20)

dice_label2 = tk.Label(dice_frame, text="-", font=("Arial", 100), bg="lightblue")

# Roll Dice Button
roll_button = tk.Button(window, text="Roll Dice", font=("Arial", 16), command=roll_dice)
roll_button.pack(pady=10)

# Option to roll one or two dice
roll_two = tk.BooleanVar()
roll_two.set(False)  # Default to rolling one dice
roll_two_checkbox = tk.Checkbutton(window, text="Roll Two Dice", variable=roll_two, font=("Arial", 14), bg="lightblue")
roll_two_checkbox.pack(pady=5)

# Dropdown to select dice color
dice_color = tk.StringVar()
dice_color.set("black")  # Default color

color_label = tk.Label(window, text="Select Dice Color:", font=("Arial", 14), bg="lightblue")
color_label.pack(pady=5)

color_menu = tk.OptionMenu(window, dice_color, "black", "red", "blue", "green", "purple")
color_menu.pack(pady=5)

# Run the main event loop
window.mainloop()

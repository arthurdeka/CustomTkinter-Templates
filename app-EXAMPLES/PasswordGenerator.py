# libraries Import
from tkinter import *
import customtkinter
import random
import string

# Function to generate password
def generate_password():
    length = 12  # Define the length of the password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    Entry_id2.delete(0, END)  # Clear the entry field
    Entry_id2.insert(0, password)  # Insert the new password

# Main Window Properties
window = Tk()
window.title("Calculator")
window.geometry("400x150")
window.configure(bg="#212121")

Entry_id2 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Generated Password",
    placeholder_text_color="#0084ff",
    font=("Arial", 14),
    text_color="#0084ff",
    height=30,
    width=360,
    border_width=2,
    corner_radius=6,
    border_color="#0084ff",
    bg_color="#212121",
    fg_color="#404040",
    )
Entry_id2.place(x=20, y=110)

Button_id1 = customtkinter.CTkButton(
    master=window,
    text="Generate Password",
    font=("Arial", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#212121",
    fg_color="#F0F0F0",
    command=generate_password  # Link the function to the button
    )
Button_id1.place(x=110, y=20)

Label_id3 = customtkinter.CTkLabel(
    master=window,
    text="Generated Password:",
    font=("Arial", 14),
    text_color="#00ccff",
    height=25,
    width=143,
    corner_radius=0,
    bg_color="#212121",
    fg_color="#212121",
    )
Label_id3.place(x=20, y=80)

# Run the main loop
window.mainloop()

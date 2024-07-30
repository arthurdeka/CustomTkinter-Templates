# libraries Import
from tkinter import *
import customtkinter
import requests

# Function to get the exchange rate USD to EUR
def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']['EUR']

# Function to convert dollars to euros
def convert_dollar_to_euro():
    dollar_amount = float(Entry_id1.get())
    rate = get_exchange_rate()
    euro_amount = dollar_amount * rate
    Label_id5.configure(text=f"{euro_amount:.2f} EUR")

# Main Window Properties
window = Tk()
window.title("Tkinter")
window.geometry("290x234")
window.configure(bg="#0f0f0f")

Entry_id1 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Value in Dollars $",
    placeholder_text_color="#fdba00",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=220,
    border_width=2,
    corner_radius=6,
    border_color="#ffbb00",
    bg_color="#0f0f0f",
    fg_color="#404040",
)
Entry_id1.place(x=30, y=120)

Label_id5 = customtkinter.CTkLabel(
    master=window,
    text="=",
    font=("Arial", 14),
    text_color="#ffffff",
    height=30,
    width=220,
    corner_radius=0,
    bg_color="#0f0f0f",
    fg_color="#0f0f0f",
)
Label_id5.place(x=40, y=160)

Button_id4 = customtkinter.CTkButton(
    master=window,
    text="Convert",
    font=("undefined", 12),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=24,
    width=220,
    border_width=2,
    corner_radius=12,
    border_color="#000000",
    bg_color="#0f0f0f",
    fg_color="#F0F0F0",
    command=convert_dollar_to_euro
)
Button_id4.place(x=30, y=200)

Label_id6 = customtkinter.CTkLabel(
    master=window,
    text="Dollar / Euro",
    font=("Impact", 24),
    text_color="#ffbb00",
    height=30,
    width=126,
    corner_radius=0,
    bg_color="#0f0f0f",
    fg_color="#0f0f0f",
)
Label_id6.place(x=80, y=30)

Label_id8 = customtkinter.CTkLabel(
    master=window,
    text="Euro €",
    font=("Arial", 14),
    text_color="#ffbb00",
    height=30,
    width=49,
    corner_radius=0,
    bg_color="#0f0f0f",
    fg_color="#0f0f0f",
)
Label_id8.place(x=30, y=160)

Label_id7 = customtkinter.CTkLabel(
    master=window,
    text="Conversor",
    font=("Courier New", 18),
    text_color="#a3a3a3",
    height=14,
    width=83,
    corner_radius=0,
    bg_color="#0f0f0f",
    fg_color="#0f0f0f",
)
Label_id7.place(x=100, y=70)

# Run the main loop
window.mainloop()

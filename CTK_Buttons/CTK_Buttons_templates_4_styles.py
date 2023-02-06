#libraries import
from tkinter import *
import customtkinter

#command function
def Click():
    pass

#Main Window properties
window = Tk()
window.title("ButtonsTemplates")
window.geometry("1030x300")
window.configure(bg="#262626")

#font definition
main_font = customtkinter.CTkFont(family="Helvetica", size=12)

#Creating the buttons
#STYLE ONE BUTTONS (FIRST ROW)
#===============================================================================
Button_StyleOne_1 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#363636",
    hover= True,
    hover_color= "#f2f2f2",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=5,
    border_color= "#d3d3d3", 
    bg_color="#262626",
    fg_color= "#fafafa")

Button_StyleOne_2 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "#3f98d7",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=5,
    border_color= "#2d6f9e", 
    bg_color="#262626",
    fg_color= "#3b8cc6")

Button_StyleOne_3 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color= "white",
    hover= True,
    hover_color= "#6fb9d5",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=5,
    border_color= "#528aa0", 
    bg_color="#262626",
    fg_color= "#68aec9")

Button_StyleOne_4 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "#81b867",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=5,
    border_color= "#608a4d", 
    bg_color="#262626",
    fg_color= "#79ae61")

Button_StyleOne_5 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "#ffb557",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=5,
    border_color= "#bc863f", 
    bg_color="#262626",
    fg_color= "#eda850")

Button_StyleOne_6 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "#e06a61",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=5,
    border_color= "#9e4a43", 
    bg_color="#262626",
    fg_color= "#c75d55")

Button_StyleOne_7 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "#454545",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=5,
    border_color= "#161616", 
    bg_color="#262626",
    fg_color= "#363636")


#STYLE TWO BUTTONS (SECOND ROW)
#===============================================================================
Button_StyleTwo_1 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=3,
    border_color= "#d3d3d3", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleTwo_2 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#3b8cc6",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=3,
    border_color= "#3b8cc6", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleTwo_3 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#68aec9",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=3,
    border_color= "#68aec9", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleTwo_4 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#79ae61",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=3,
    border_color= "#79ae61", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleTwo_5 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#eda850",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=3,
    border_color= "#eda850", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleTwo_6 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#c75d55",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=3,
    border_color= "#c75d55", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleTwo_7 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=3,
    border_color= "black", 
    bg_color="#262626",
    fg_color= "#262626")


#STYLE THREE BUTTONS (THIRD ROW)
#===============================================================================
Button_StyleThree_1 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#d3d3d3", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleThree_2 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#3b8cc6",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#3b8cc6", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleThree_3 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#68aec9",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#68aec9", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleThree_4 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#79ae61",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#79ae61", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleThree_5 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#eda850",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#eda850", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleThree_6 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#c75d55",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#c75d55", 
    bg_color="#262626",
    fg_color= "#262626")

Button_StyleThree_7 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "black", 
    bg_color="#262626",
    fg_color= "#262626")


#STYLE FOUR BUTTONS (FOUTH ROW)
#===============================================================================
Button_StyleFour_1 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="#363636",
    hover= True,
    hover_color= "#f2f2f2",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#d3d3d3", 
    bg_color="#262626",
    fg_color= "#fafafa")

Button_StyleFour_2 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "#3f98d7",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#2d6f9e", 
    bg_color="#262626",
    fg_color= "#3b8cc6")

Button_StyleFour_3 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color= "white",
    hover= True,
    hover_color= "#6fb9d5",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#528aa0", 
    bg_color="#262626",
    fg_color= "#68aec9")

Button_StyleFour_4 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "#81b867",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#608a4d", 
    bg_color="#262626",
    fg_color= "#79ae61")

Button_StyleFour_5 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "#ffb557",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#bc863f", 
    bg_color="#262626",
    fg_color= "#eda850")

Button_StyleFour_6 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "#e06a61",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#9e4a43", 
    bg_color="#262626",
    fg_color= "#c75d55")

Button_StyleFour_7 = customtkinter.CTkButton(
    master= window,
    command= Click,
    text= "Click Me",
    font= main_font,
    text_color="white",
    hover= True,
    hover_color= "#454545",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#161616", 
    bg_color="#262626",
    fg_color= "#363636")


#placing the buttons
#===================================================================
#FIRST ROW
Button_StyleOne_1.place(x= 15, y= 15)
Button_StyleOne_2.place(x= 160, y= 15)
Button_StyleOne_3.place(x= 305, y= 15)
Button_StyleOne_4.place(x= 450, y= 15)
Button_StyleOne_5.place(x= 595, y= 15)
Button_StyleOne_6.place(x= 740, y= 15)
Button_StyleOne_7.place(x= 885, y= 15)
#SECOND ROW
Button_StyleTwo_1.place(x= 15, y= 90)
Button_StyleTwo_2.place(x= 160, y= 90)
Button_StyleTwo_3.place(x= 305, y= 90)
Button_StyleTwo_4.place(x= 450, y= 90)
Button_StyleTwo_5.place(x= 595, y= 90)
Button_StyleTwo_6.place(x= 740, y= 90)
Button_StyleTwo_7.place(x= 885, y= 90)
#THIRD ROW
Button_StyleThree_1.place(x= 15, y= 165)
Button_StyleThree_2.place(x= 160, y= 165)
Button_StyleThree_3.place(x= 305, y= 165)
Button_StyleThree_4.place(x= 450, y= 165)
Button_StyleThree_5.place(x= 595, y= 165)
Button_StyleThree_6.place(x= 740, y= 165)
Button_StyleThree_7.place(x= 885, y= 165)
#FOUTH ROW
Button_StyleFour_1.place(x= 15, y= 240)
Button_StyleFour_2.place(x= 160, y= 240)
Button_StyleFour_3.place(x= 305, y= 240)
Button_StyleFour_4.place(x= 450, y= 240)
Button_StyleFour_5.place(x= 595, y= 240)
Button_StyleFour_6.place(x= 740, y= 240)
Button_StyleFour_7.place(x= 885, y= 240)

#run the main loop
window.mainloop()
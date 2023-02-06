#custom buttons templates
from tkinter import *
import customtkinter

#command function
def Click():
    pass

#Main Window properties
window = Tk()
window.title("EntrysTemplates")
window.geometry("280x515")
window.configure(bg="#262626")

#font definition
main_font = customtkinter.CTkFont(family="Helvetica", size=12)

#Creating the entrys
#style 1
entry_1 = customtkinter.CTkEntry(master=window,
                               placeholder_text="CTkEntry",
                               placeholder_text_color="#cccccc",
                               
                               font= main_font,
                               text_color="white",
                               
                               width=220,
                               height=30,
                               border_width=2,
                               border_color= "#d3d3d3",
                               bg_color="#262626",
                               fg_color= "#262626",
                               
                               corner_radius=5)
entry_2 = customtkinter.CTkEntry(master=window,
                               placeholder_text="CTkEntry",
                               placeholder_text_color="#3b8cc6",
                               
                               font= main_font,
                               text_color="#3b8cc6",
                               
                               width=220,
                               height=30,
                               border_width=2,
                               border_color= "#3b8cc6",
                               bg_color="#262626",
                               fg_color= "#262626",
                               
                               corner_radius=5)
entry_3 = customtkinter.CTkEntry(master=window,
                               placeholder_text="CTkEntry",
                               placeholder_text_color="#79ae61",
                               
                               font= main_font,
                               text_color="#79ae61",
                               
                               width=220,
                               height=30,
                               border_width=2,
                               border_color= "#79ae61",
                               bg_color="#262626",
                               fg_color= "#262626",
                               
                               corner_radius=5)
entry_4 = customtkinter.CTkEntry(master=window,
                               placeholder_text="CTkEntry",
                               placeholder_text_color="#eda850",
                               
                               font= main_font,
                               text_color="#eda850",
                               
                               width=220,
                               height=30,
                               border_width=2,
                               border_color= "#eda850",
                               bg_color="#262626",
                               fg_color= "#262626",
                               
                               corner_radius=5)
entry_5 = customtkinter.CTkEntry(master=window,
                               placeholder_text="CTkEntry",
                               placeholder_text_color="#c75d55",
                               
                               font= main_font,
                               text_color="#c75d55",
                               
                               width=220,
                               height=30,
                               border_width=2,
                               border_color= "#c75d55",
                               bg_color="#262626",
                               fg_color= "#262626",
                               
                               corner_radius=5)

#style 2
entry_6 = customtkinter.CTkEntry(master=window,
                               placeholder_text="CTkEntry",
                               placeholder_text_color="black",
                               
                               font= main_font,
                               text_color="black",
                               
                               width=220,
                               height=30,
                               border_width=2,
                               border_color= "black",
                               bg_color="#262626",
                               fg_color= "#EEEEEE",
                               
                               corner_radius=5)
entry_7 = customtkinter.CTkEntry(master=window,
                               placeholder_text="CTkEntry",
                               placeholder_text_color="black",
                               
                               font= main_font,
                               text_color="black",
                               
                               width=220,
                               height=30,
                               border_width=2,
                               border_color= "black",
                               bg_color="#262626",
                               fg_color= "#2E8BC0",
                               
                               corner_radius=5)
entry_8 = customtkinter.CTkEntry(master=window,
                               placeholder_text="CTkEntry",
                               placeholder_text_color="black",
                               
                               font= main_font,
                               text_color="black",
                               
                               width=220,
                               height=30,
                               border_width=2,
                               border_color= "black",
                               bg_color="#262626",
                               fg_color= "#79ae61",
                               
                               corner_radius=5)
entry_9 = customtkinter.CTkEntry(master=window,
                               placeholder_text="CTkEntry",
                               placeholder_text_color="black",
                               
                               font= main_font,
                               text_color="black",
                               
                               width=220,
                               height=30,
                               border_width=2,
                               border_color= "black",
                               bg_color="#262626",
                               fg_color= "#eda850",
                               
                               corner_radius=5)
entry_10 = customtkinter.CTkEntry(master=window,
                               placeholder_text="CTkEntry",
                               placeholder_text_color="black",
                               
                               font= main_font,
                               text_color="black",
                               
                               width=220,
                               height=30,
                               border_width=2,
                               border_color= "black",
                               bg_color="#262626",
                               fg_color= "#c75d55",
                               
                               corner_radius=5)


#placing the resources
entry_1.place(x= 30, y= 30)
entry_2.place(x= 30, y= 75)
entry_3.place(x= 30, y= 120)
entry_4.place(x= 30, y= 165)
entry_5.place(x= 30, y= 210)

entry_6.place(x= 30, y= 280)
entry_7.place(x= 30, y= 325)
entry_8.place(x= 30, y= 370)
entry_9.place(x= 30, y= 415)
entry_10.place(x= 30, y= 460)


#run the main loop
window.mainloop()
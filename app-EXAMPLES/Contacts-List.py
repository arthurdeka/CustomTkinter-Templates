import tkinter
import customtkinter

#function to add the contact
def add_contact():
    nome = name_entry.get()
    telefone = tel_entry.get()
    
    #Adds contact data to listbox
    contacts_listbox.insert(tkinter.END, nome + " - " + telefone)
    
    #Clears entries data
    name_entry.delete(0, tkinter.END)
    tel_entry.delete(0, tkinter.END)

#creates the main window
window = tkinter.Tk()
window.configure(bg='#262626')
window.title("Contact List")

#Creates a frame to hold the widgets
frame = tkinter.Frame(window, background='#262626')
frame.pack()

#Creates labels for name and tel
name_label = customtkinter.CTkLabel(
                                master=frame,
                                text="Name:",
                                text_color= "black",
                                width=120,
                                height=25,
                                fg_color=("white", "gray75"),
                                bg_color="#262626",
                                corner_radius=8)
name_label.grid(row=0, column=0, padx=7, pady=10)


tel_label = customtkinter.CTkLabel(
                                master=frame,
                                text="Tel:",
                                text_color= "black",
                                width=120,
                                height=25,
                                fg_color=("white", "gray75"),
                                bg_color="#262626",
                                corner_radius=8)
tel_label.grid(row=1, column=0)

#Creates entries for name and phone
name_entry = customtkinter.CTkEntry(
                                master=frame,
                                text_color="white",
                               
                                border_width=2,
                                border_color= "#d3d3d3",
                                bg_color="#262626",
                                fg_color= "#262626",
                               
                                corner_radius=5)
name_entry.grid(row=0, column=1, padx=7)


tel_entry = customtkinter.CTkEntry(
                                master=frame,
                                text_color="white",
                               
                                border_width=2,
                                border_color= "#d3d3d3",
                                bg_color="#262626",
                                fg_color= "#262626",
                               
                                corner_radius=5)
tel_entry.grid(row=1, column=1)

#Creates a button to add a new contact
add_button = customtkinter.CTkButton(
    master= frame,
    command= add_contact,
    text= "Add",
    text_color="white",
    hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "black", 
    bg_color="#262626",
    fg_color= "#262626",
    )
add_button.grid(row=2, column=0, columnspan=2, pady=15)


# Creates a listbox to show contacts
contacts_listbox = tkinter.Listbox(window, bg="#262626", fg="white")
contacts_listbox.pack()


window.mainloop()

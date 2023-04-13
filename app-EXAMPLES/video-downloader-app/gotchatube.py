import tkinter
import customtkinter
#video downloader library
from pytube import YouTube


#video download function
def downloadVideo():
    url = customtkinter.CTkEntry.get(videoURL)
    exit_dir = customtkinter.CTkEntry.get(exitPath)
    
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path = exit_dir)


#creates the main window
window = tkinter.Tk()
window.title("GotchaTube!")
window.geometry("530x165")
window.resizable(width = False ,height = False)
window.configure(bg='#252525')


#creating the widgets
logo = tkinter.PhotoImage(file="logo.png")
label_logo = tkinter.Label(window, image=logo, bd=0)

videoURL = customtkinter.CTkEntry(
    master=window,
    placeholder_text='Enter video URL here',
    width= 345,
    height=35,
)
exitPath = customtkinter.CTkEntry(
    master=window,
    placeholder_text='File exit path',
    width= 345,
    height=35,
)

downloadButton = customtkinter.CTkButton(
    master=window,
    command=downloadVideo,
    text="Download",
    text_color="white",
    hover= True,
    hover_color= "black",
    height=35,
    width= 120,
    border_width=2,
    corner_radius=4,
    border_color= "#5d6266", 
    bg_color="#262626",
    fg_color= "#262626",
)


#placing the widgets
label_logo.place(x= 22, y= 18)
videoURL.place(x= 18, y= 65)
exitPath.place(x= 18, y= 110)
downloadButton.place(x= 380, y= 110)


#running the app
window.mainloop()
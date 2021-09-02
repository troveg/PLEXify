from tkinter import *
from PIL import Image, ImageTk
import tkinter.filedialog, os, glob

# Window
root = Tk()
root.geometry("600x450")
root.title("PLEXify")
root.iconbitmap("icon.ico")
root.configure(bg="#1f1f1f")

# Variables
media_type = "Anime"
season = 1
anime_file = [".mkv", ".mp4", ".avi"]
manga_file = [".cbz", ".cbr", ".zip"]
file_select = 0
file_type = anime_file[file_select]
title = StringVar()

# Images
logo = ImageTk.PhotoImage(Image.open("plex.png"))
plus = ImageTk.PhotoImage(Image.open("plus.png"))

def main():
    global season, media_type, title, file_type

    def season_add():
        global season
        season += 1
        status_season.configure(text=("Season: " + str(season)))
    def season_sub():
        global season
        season -= 1
        status_season.configure(text=("Season: " + str(season)))
    def media_switch():
        global media_type, file_select
        if media_type == "Anime":
            media_type = "Manga"
        else:
            media_type = "Anime"
        file_select -= 1
        file_change()
        status_type.configure(text=("Media Type: " + media_type))
    def file_change():
        global file_select, file_type, media_type
        file_select += 1
        if file_select > 2:
            file_select = 0
        if media_type == "Anime":
            file_type = anime_file[file_select]
        else:
            file_type = manga_file[file_select]
        status_file.configure(text=("File Type: " + file_type))
    def plexify():
        global title, season, file_type
        file_number = 0
        plex_title = title.get()
        directory = tkinter.filedialog.askdirectory()
        os.chdir(directory)
        if media_type == "Anime":
            season = str(season)
            if int(season) < 10:
                season = "0" + season
            for file in glob.glob("*" + file_type):
                file_number = int(file_number)
                file_number += 1
                if file_number < 10:
                    file_number = "0" + str(file_number)
                else:
                    file_number = str(file_number)
                file2 = plex_title + " - S" + season + "E" + file_number + file_type
                os.rename(file, file2)
        else:
            for file in glob.glob("*" + file_type):
                file_number = int(file_number)
                file_number += 1
                file_number = str(file_number)
                file2 = plex_title + " {Vol-" + file_number + "}" + file_type
                os.rename(file, file2)

    # Frames
    entry_frame = Frame(root, bg="#202020", bd=5, relief=RIDGE)
    plex_frame = Frame(root, bg="#202020", width=267, height=90)
    status_frame = Frame(root, bg="gray", width=400, height=20)

    # Entry
    media_entry = Entry(entry_frame, textvariable=title, width=30).pack(anchor='center')
    Label(root, text="Title: ", bg="#202020", fg="white", bd=5).place(x=65, y=140)

    # Buttons
    switch_button = Button(root, width=10, text="Switch", command=media_switch, bg="gray", fg="white")
    file_button = Button(root, width=10, text="File", command=file_change, bg="gray", fg="white")
    season_down = Button(root, text="-", command=season_sub, bg="gray", fg="white")
    season_up = Button(root, image=plus, command=season_add, bg="gray", fg="white")
    rename_button = Button(root, width=26, text="PLEXify", command=plexify, bg="gray", fg="white")

    # Status
    Label(plex_frame, image=logo).place(x=(-2), y=(-2))
    status_type = Label(status_frame, bg="gray", fg="white", text=("Media Type: " + media_type))
    status_file = Label(status_frame, bg="gray", fg="white", text=("File Type: " + file_type))
    status_season = Label(status_frame, bg="gray", fg="white", text=("Season: " + str(season)))

    # Placements
    switch_button.place(x=105, y=170)
    file_button.place(x=185, y=170)
    season_down.place(x=265, y=170)
    season_up.place(x=281, y=170)
    rename_button.place(x=106, y=196)
    status_type.place(x=35, y=0)
    status_file.place(x=172)
    status_season.place(x=285, y=0)
    entry_frame.place(x=105, y=140)
    plex_frame.place(x=72, y=26)
    status_frame.place(x=0, y=280)

main()
root.mainloop()
from tkinter import *
from tkinter import filedialog, ttk
import pygame.mixer as mixer
import os

mixer.init()

# Define a list of supported audio file extensions
SUPPORTED_FORMATS = ['.mp3', '.wav']

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    selected_song = songs_list.get(ACTIVE)

    # Check if the selected file has a supported audio format
    if os.path.splitext(selected_song)[1].lower() not in SUPPORTED_FORMATS:
        status.set("Unsupported Format")
        return

    song_name.set(selected_song)

    mixer.music.load(selected_song)
    mixer.music.play()

    status.set("Song PLAYING")

def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))

    tracks = os.listdir()

    for track in tracks:
        if os.path.splitext(track)[1].lower() in SUPPORTED_FORMATS:
            listbox.insert(END, track)

from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

mixer.init()

# Define a list of supported audio file extensions
SUPPORTED_FORMATS = ['.mp3', '.wav']

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    selected_song = songs_list.get(ACTIVE)

    # Check if the selected file has a supported audio format
    if os.path.splitext(selected_song)[1].lower() not in SUPPORTED_FORMATS:
        status.set("Unsupported Format")
        return

    song_name.set(selected_song)

    mixer.music.load(selected_song)
    mixer.music.play()

    status.set("Song PLAYING")

def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))

    tracks = os.listdir()

    for track in tracks:
        if os.path.splitext(track)[1].lower() in SUPPORTED_FORMATS:
            listbox.insert(END, track)

def next_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    # Get the currently selected song index
    current_index = songs_list.curselection()
    if current_index:
        # Get the index of the next song (add 1 to the current index)
        next_index = current_index[0] + 1
        # Check if the next song index is within the bounds of the playlist
        if next_index < songs_list.size():
            songs_list.select_clear(0, END)  # Clear the current selection
            songs_list.activate(next_index)  # Activate the next song
            songs_list.selection_set(next_index)  # Set the next song as selected
            # Play the next song
            play_song(song_name, songs_list, status)

def previous_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    # Get the currently selected song index
    current_index = songs_list.curselection()
    if current_index:
        # Get the index of the previous song (subtract 1 from the current index)
        previous_index = current_index[0] - 1
        # Check if the previous song index is within the bounds of the playlist
        if previous_index >= 0:
            songs_list.select_clear(0, END)  # Clear the current selection
            songs_list.activate(previous_index)  # Activate the previous song
            songs_list.selection_set(previous_index)  # Set the previous song as selected
            # Play the previous song
            play_song(song_name, songs_list, status)

# Create a function to switch between screens
def show_screen(screen):
    current_screen.pack_forget()
    screen.pack()

root = Tk()
root.geometry('700x220')
root.title("My Music Player")
root.resizable(0, 0)

# Create a tabbed interface using a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand='yes')

# Create screens as frames
current_screen = Frame(notebook)
playlist_screen = Frame(notebook)

# Add screens to the notebook
notebook.add(current_screen, text='Current Song')
notebook.add(playlist_screen, text='Playlist')

# Set the default screen to display
show_screen(current_screen)

def previous_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    # Get the currently selected song index
    current_index = songs_list.curselection()
    if current_index:
        # Get the index of the previous song (subtract 1 from the current index)
        previous_index = current_index[0] - 1
        # Check if the previous song index is within the bounds of the playlist
        if previous_index >= 0:
            songs_list.select_clear(0, END)  # Clear the current selection
            songs_list.activate(previous_index)  # Activate the previous song
            songs_list.selection_set(previous_index)  # Set the previous song as selected
            # Play the previous song
            play_song(song_name, songs_list, status)

song_frame = LabelFrame(root, text='Current Song',font=("Comic Sans MS", 11, "bold"), fg="black", width=400, height=80)

song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons',font=("Comic Sans MS", 11, "bold"), fg="black", width=400, height=120)

button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Playlist',font=("Comic Sans MS", 11, "bold"), fg="black")

listbox_frame.place(x=400, y=0, height=200, width=300)

current_song = StringVar(root, value='<Not selected>')

song_status = StringVar(root, value='<Not Available>')

playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)

scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)

song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
song_lbl.place(x=150, y=20)

pause_btn = Button(button_frame, text='Play', bg='#07ad02', font=("Georgia", 13), width=7,
                   command=lambda: play_song(song_status, playlist, song_status))
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: pause_song(song_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text='Resume', bg='#007bff', font=("Georgia", 13), width=7,
                  command=lambda: resume_song(current_song))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text='Stop', bg='#ff0000', font=("Georgia", 13), width=7,
                    command=lambda: stop_song(song_status))
resume_btn.place(x=285, y=10)

previous_btn = Button(button_frame, text='Previous', bg='#ff9900', font=("Georgia", 13), width=7,
                      command=lambda: previous_song(current_song, playlist, song_status))
previous_btn.place(x=285, y=10)


next_btn = Button(button_frame, text='Next', bg='#ff9900', font=("Georgia", 13), width=7,
                  command=lambda: next_song(current_song, playlist, song_status))
next_btn.place(x=50, y=55)

load_btn = Button(button_frame, text='Open Folder ', bg='#0c74ae', font=("Georgia", 13), width=15,
                  command=lambda: load(playlist))
load_btn.place(x=150, y=55)

root.update()

root.mainloop()
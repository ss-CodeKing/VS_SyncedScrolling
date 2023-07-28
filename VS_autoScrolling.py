import tkinter as tk
from tkinter import font
from mutagen.mp3 import MP3
import subprocess
import time

# Create the main window
window = tk.Tk()
window.title("Vishnu Sahasaranama Stotram")
window.geometry("900x700")
window.configure(bg="black")

# Define the font and font size
custom_font = font.Font(family="Lohit Devanagari", size=16)

# Add a scrolling area to display the text content
text_widget = tk.Text(window, wrap=tk.WORD, font=custom_font, fg="white", bg="black")
text_widget.pack(fill=tk.BOTH, expand=True)

# Load the text content from file
text_file_path = "VishnuSahasaranamam.txt"
with open(text_file_path, "r", encoding="utf-8") as file:
    iast_text = file.read()
text_widget.insert(tk.END, iast_text)

# Load the audio file
audio_file_path = "Vishnu Sahasranamam.mp3"


# Find the length of the audio
def get_audio_length(audio_file_path):
    audio = MP3(audio_file_path)
    duration = audio.info.length
    return duration


# Start auto scroll
def start_auto_scroll(audio_length, start_time):
    current_time = time.time() - start_time
    scroll_position = current_time / audio_length
    text_widget.yview_moveto(scroll_position)
    if current_time < audio_length:
        window.after(100, start_auto_scroll, audio_length, start_time)
    else:
        pass  # Audio playback is completed, stop auto-scrolling


# Function to launch audio
def play_audio():
    subprocess.Popen(["explorer.exe", audio_file_path])
    audio_length = get_audio_length(audio_file_path)
    start_auto_scroll(audio_length, start_time=time.time())


# Button to start audio playback
start_button = tk.Button(window, text="Start", command=play_audio)
start_button.pack()

# Start the Tkinter event loop
window.mainloop()

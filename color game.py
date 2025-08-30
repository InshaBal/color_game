import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os

# --- Global Variables ---
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'Purple', 'Brown', 'Gray']
score = 0
timeleft = 30
game_started = False

# --- Functions ---
def start_game():
    global game_started, timeleft, score
    if not game_started:
        game_started = True
        timeleft = 30
        score = 0
        score_label.config(text="Score: 0")
        time_label.config(text="Time left: 30")
        progress_bar['value'] = 100
        label.config(text="")
        entry.delete(0, tk.END)
        next_color()
        countdown()

def next_color():
    global score
    if timeleft > 0:
        entry.focus_set()
        if entry.get().lower() == colors[1].lower():
            score += 1
        entry.delete(0, tk.END)
        random.shuffle(colors)
        label.config(fg=colors[1], text=colors[0])
        score_label.config(text="Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        time_label.config(text="Time left: " + str(timeleft))
        progress_bar['value'] = (timeleft / 30) * 100
        root.after(1000, countdown)
    else:
        end_game()

def end_game():
    global game_started
    label.config(text="Game Over!", fg="red")
    entry.delete(0, tk.END)
    game_started = False

def submit(event=None):
    if game_started and timeleft > 0:
        next_color()

def reset_game():
    global timeleft, score, game_started
    score = 0
    timeleft = 30
    game_started = True
    score_label.config(text="Score: 0")
    time_label.config(text="Time left: 30")
    progress_bar['value'] = 100
    label.config(text="")
    entry.delete(0, tk.END)
    next_color()
    countdown()

# --- GUI Setup ---
root = tk.Tk()
root.title("🎨 Color Game")
root.geometry("520x580")
root.resizable(False, False)

# --- Set Icon ---
if os.path.exists("icon.ico"):
    root.iconbitmap("icon.ico")

# --- Set Background Image ---
if os.path.exists("bg.png"):
    bg_image = Image.open("bg.png")
    bg_image = bg_image.resize((520, 580))
    bg_photo = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(root, image=bg_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    root.configure(bg="#121212")  # fallback to dark

# --- Styling ---
FONT_TITLE = ('Helvetica', 30, 'bold')
FONT_INSTRUCTION = ('Helvetica', 14, 'bold')
FONT_MAIN = ('Helvetica', 13, 'bold')
FONT_BIG = ('Helvetica', 44, 'bold')
FONT_INPUT = ('Helvetica', 22)
FG_COLOR = "white"
BTN_COLOR = "#00BFFF"

# --- Title ---
title = tk.Label(root, text="🎨 COLOR GAME", font=FONT_TITLE, bg="#121212", fg=BTN_COLOR)
title.place(relx=0.5, y=30, anchor='center')

# --- Labels ---
instructions = tk.Label(root, text="Type the COLOR of the text, not the word!",
                        font=FONT_INSTRUCTION, bg="#121212", fg=FG_COLOR)
instructions.place(relx=0.5, y=80, anchor='center')

score_label = tk.Label(root, text="Score: 0", font=FONT_MAIN, bg="#121212", fg=FG_COLOR)
score_label.place(relx=0.5, y=110, anchor='center')

time_label = tk.Label(root, text="Time left: 30", font=FONT_MAIN, bg="#121212", fg="#FF5555")
time_label.place(relx=0.5, y=140, anchor='center')

# --- Countdown Bar ---
progress_bar = ttk.Progressbar(root, length=400, mode='determinate')
progress_bar.place(relx=0.5, y=170, anchor='center')

# --- Color Word ---
label = tk.Label(root, font=FONT_BIG, bg="#121212")
label.place(relx=0.5, y=230, anchor='center')

# --- Input ---
entry = tk.Entry(root, font=FONT_INPUT, justify='center', bg="#1a1a1a", fg="white", insertbackground="white", width=20)
entry.bind('<Return>', submit)
entry.place(relx=0.5, y=300, anchor='center', height=45)

# --- Buttons ---
btn_frame = tk.Frame(root, bg="#121212")
btn_frame.place(relx=0.5, y=390, anchor='center')

button_style = {
    "font": ('Helvetica', 13, 'bold'),
    "bg": BTN_COLOR,
    "fg": "white",
    "activebackground": "#009ACD",
    "width": 12,
    "height": 2,
    "bd": 0,
    "relief": "flat",
    "cursor": "hand2"
}

start_button = tk.Button(btn_frame, text="▶ Start", command=start_game, **button_style)
start_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(btn_frame, text="🔁 Reset", command=reset_game, **button_style)
reset_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(btn_frame, text="❌ Exit", command=root.quit, **button_style)
exit_button.grid(row=0, column=2, padx=10)

entry.focus_set()
root.mainloop()

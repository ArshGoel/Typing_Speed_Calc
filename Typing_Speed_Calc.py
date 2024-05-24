#---------------------Import Statements------------------#
from tkinter import *
import random
import time
from tkinter import font
from ttkthemes import ThemedTk      ########-------pip install ttkthemes-------######
from tkinter import ttk


def start_input():
    global current_sentence, start_time
    current_sentence = random.choice(sentences)
    prompt_entry.delete("1.0", END)
    prompt_entry.insert(END, current_sentence)
    input_entry.delete("1.0",END)
    start_time = time.time()
    start_button.config(state="disabled")
    stop_button.config(state="normal")
    reset_button.config(state="disabled")

def stop_input():
    global stop_time
    stop_time = time.time()
    calculate_wpm_and_accuracy()
    stop_button.config(state="disabled")
    reset_button.config(state="normal")

def reset_input():
    global current_sentence, start_time, stop_time
    current_sentence = ""
    start_time = 0
    stop_time = 0
    prompt_entry.delete("1.0", END)
    input_entry.delete("1.0", END)
    result_label.config(text="")
    start_button.config(state="normal")
    stop_button.config(state="disabled")
    reset_button.config(state="disabled")

def calculate_wpm_and_accuracy():
    
    user_input = input_entry.get("1.0", END)
    user_input = user_input.strip()
    words_typed = len(user_input.split())
    time_taken = stop_time - start_time
    wpm = words_typed / (time_taken / 60)
    accuracy = calculate_accuracy(user_input, current_sentence)
    result_label.config(text=f"Your typing speed is: {wpm:.2f} WPM\nYour accuracy is: {accuracy:.2f}%")

def calculate_accuracy(user_input, current_sentence):
    correct_chars = 0
    for i in range(min(len(user_input), len(current_sentence))):
        if user_input[i] == current_sentence[i]:
            correct_chars += 1
    accuracy = (correct_chars / len(current_sentence)) * 100
    return accuracy

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How vexingly quick waltzing zebras jump!",
    "Bright vixens jump; dozy fowl quack.",
    "Quick wafting zephyrs vex bold Jim.",
    "How quickly wizards zap xylophones.",
    "Pack five dozen liquor jugs in my box.",
    "The five boxing wizards jump quickly.",
    "How quickly wizards jump at foggy quartz.",
    "Bright vixens jump; dozy fowl quack loudly."
]

root = ThemedTk(theme="adapta")
root.iconbitmap(r"F:\PYTHON\Internship\Typing Speed Calculator\logo.ico")
root.title("Typing Speed Calculator")

font1 = font.Font(family='Lucida Calligraphy',size=12)

prompt_label = ttk.Label(root,font=font1 ,text="Type the following sentence:")
prompt_label.pack()

prompt_entry = Text(root,font=font1, height=1, width=50)
prompt_entry.pack()

input_entry = Text(root,font=font1, height=5, width=50)
input_entry.pack()

current_sentence = ""
start_time = 0
stop_time = 0

start_button = ttk.Button(root, text="Start", command=start_input)
start_button.pack()

stop_button = ttk.Button(root, text="Stop", command=stop_input, state="disabled")
stop_button.pack()

reset_button = ttk.Button(root, text="Reset", command=reset_input, state="disabled")
reset_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
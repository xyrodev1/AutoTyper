import time
import pyautogui
from customtkinter import *
import random
from tkinter import messagebox
import os

def main():
    def humanerror():
        incorrect_char = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.?/;:")
        if random.random() < humanerroramount.get():
            pyautogui.typewrite(incorrect_char)
            time.sleep(0.3)
            pyautogui.press('backspace')

    def start_typing():
        messagebox.showinfo("Typer", "Starting Typing")
        entered_text = textfortyping.get("1.0", "end")
        wpmz = wpmamount.get()
        wpm = float(wpmz)
        word = entered_text.split()
        for word in entered_text:
            pyautogui.typewrite(word)
            time.sleep(60 / (float(wpm) * 5))
            switchv = switch.get()
            if switchv == True: 
                humanerror()

    def slider(value):
        wpmamountshowing.configure(text=f"WPM: {value:.2f}")

    def update_humanerrorslider(value):
        humanerrorshowing.configure(text=f"Human Error: {value:.2f}%")

    app = CTk()
    set_appearance_mode("Dark")
    app.title("Typer")
    app.geometry("1000x900")
    app.resizable(False, False)
    try:
        icon_path = os.path.join(os.path.dirname(__file__), "keyboard.ico")
        app.iconbitmap(icon_path)
    except Exception as e:
        print(f"Icon not found: {e}")
    
    title = CTkLabel(master=app, text="Typer", text_color="#EAEAEA", font=("Arial", 40))

    wpmamount = CTkSlider(master=app, command=slider, from_=0, to=200)
    wpmamountshowing = CTkLabel(master=app, text="Edit The Slider To Change The WPM", text_color="#EAEAEA")
    humanerroramount = CTkSlider(master=app, command=update_humanerrorslider, from_=0, to=50)
    humanerrorshowing = CTkLabel(master=app, text="Edit The Slider To Change The Human Error Higher = More error Lower = less error", text_color="#EAEAEA")

    switch = CTkSwitch(master=app, text="Human Error", fg_color="#444444", text_color="white")

    textfortyping = CTkTextbox(master=app, width=300, fg_color="#2A2A2A", text_color="#EAEAEA")

    start_button = CTkButton(master=app, text="Start", corner_radius=32, fg_color="#444444", hover_color="#333333", command=start_typing)

    textfortyping.place(relx=0.3, rely=0.1)
    start_button.place(relx=0.45, rely=0.5, anchor="center")
    textfortyping = CTkTextbox(master=app, width=300, fg_color="#2A2A2A", text_color="#EAEAEA")

    # Start Button
    start_button = CTkButton(master=app, text="Start", corner_radius=32, fg_color="#444444", hover_color="#333333", command=start_typing)

    # Layout
    textfortyping.place(relx=0.3, rely=0.1)
    start_button.place(relx=0.45, rely=0.5, anchor="center")
    wpmamount.place(relx=0.34, rely=0.35)
    wpmamountshowing.place(relx=0.34, rely=0.32)
    title.place(relx=0.39, rely=0)
    switch.place(relx=0.39, rely=0.38)
    humanerroramount.place(relx=0.34, rely=0.45)
    humanerrorshowing.place(relx=0.34, rely=0.42)

    app.mainloop()

if __name__ == "__main__":
    main()

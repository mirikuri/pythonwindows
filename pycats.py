import os
import ctypes
import random
import time
import pyautogui
import tkinter as tk
from tkinter import messagebox
from threading import Thread

def set_wallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

def random_mouse():
    while True:
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(2)

def popup():
    messages = [
        "Ты лучший!",
        "Я тебя вижу 😏",
        "Это не сон",
        "Добро пожаловать в клуб котиков",
        "Ты заражён… любовью 🥰"
    ]
    for msg in messages:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Вирус", msg)
        time.sleep(1)

def main():
    img_path = os.path.abspath("kitten.jpg")
    set_wallpaper(img_path)

    Thread(target=random_mouse, daemon=True).start()
    popup()

if __name__ == "__main__":
    main()

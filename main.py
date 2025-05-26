import threading
import tkinter as tk
import os
from PIL import Image, ImageTk
from utils.util_services import execute_command
from utils.disk_clear import disk_clear
from tkinter import PhotoImage


def on_click():
    def wrapped():
        global is_executing
        is_executing = True
        execute_button.config(state="disabled")
        
        try:
            if torf_disk.get():
                disk_clear()
            execute_command()
        except Exception as e:
            print(f"Erro ao executar comando: {e}")
        finally:
            execute_button.config(state="normal")
            is_executing = False

    threading.Thread(target=wrapped, daemon=True).start()

def toggle_checkbox(event = None):
        if is_executing == True:
            return
        if torf_disk.get() == 0:
            torf_disk.set(1)
            disk_label.config(image = checkbox_image)
        else:
            torf_disk.set(0)
            disk_label.config(image = uncheckbox_image)


window = tk.Tk()

is_executing = False

window.title("Black Desert Optimizer (by ZXCASDQWEASDZXC)")
window.geometry("680x402")
window.resizable(False, False)

background_path = os.path.join("icons", "bg_main.png")
original_background_image = Image.open(background_path).resize((680, 402))
background_image = ImageTk.PhotoImage(original_background_image)

background_label = tk.Label(window, image=background_image, bg="#222229")
background_label.place(x=0, y=0, relwidth=1, relheight=1)


checkbox_path = os.path.join("icons", "checkbox_check.png")
image_checkbox_checked = Image.open(checkbox_path).resize((30, 30))
checkbox_image = ImageTk.PhotoImage(image_checkbox_checked)


uncheckbox_path = os.path.join("icons", "checkbox_uncheck.png")
image_checkbox_unchecked = Image.open(uncheckbox_path).resize((30, 30))
uncheckbox_image = ImageTk.PhotoImage(image_checkbox_unchecked)

torf_disk = tk.IntVar(value=0)
disk_label = tk.Label(window, image = uncheckbox_image,bd=0, highlightthickness=0)
disk_label.pack(side='bottom', anchor='e', padx=220, pady=37)

disk_label.bind("<Button-1>", toggle_checkbox)       

button_image_path = os.path.join("icons", "button_execute.png")
original_button_image = Image.open(button_image_path)
button_image = ImageTk.PhotoImage(original_button_image)

execute_button = tk.Button(
    window,
    image=button_image,
    command=on_click,
    bg="#1e1e1e",
    bd=0
)

execute_button.image = button_image
execute_button.place(relx=1.0, rely=1.0, anchor="se", x=-25, y=-25)

window.mainloop()
import threading
import tkinter as tk
import os
from PIL import Image, ImageTk
from utils.util_services import execute_command
from utils.disk_clear import disk_clear


def on_click():
    def wrapped():
        execute_button.config(state="disabled")
        try:
            if torf_disk.get():
                disk_clear()
            execute_command()
        except Exception as e:
            print(f"Erro ao executar comando: {e}")
        finally:
            execute_button.config(state="normal")

    threading.Thread(target=wrapped, daemon=True).start()



window = tk.Tk()
window.title("Black Desert Optimizer (by ZXCASDQWEASDZXC)")
window.geometry("680x402")
window.resizable(False, False)

background_path = os.path.join("icons", "bg_main.png")
original_background_image = Image.open(background_path)
resized_background_image = original_background_image.resize((680, 402))
background_image = ImageTk.PhotoImage(resized_background_image)

background_label = tk.Label(window, image=background_image, bg="#222229")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

button_image_path = os.path.join("icons", "button_execute.png")
original_button_image = Image.open(button_image_path)
button_image = ImageTk.PhotoImage(original_button_image)

torf_disk = tk.IntVar()
disk_check = tk.Checkbutton(
    window, 
    text="Limpar disco.", 
    variable=torf_disk
)
disk_check.pack(padx=30, pady=30)

execute_button = tk.Button(
    window,
    image=button_image,
    command=on_click,
    bg="#1e1e1e",
    bd=0,
    activebackground="#1e1e1e"
)

execute_button.image = button_image
execute_button.place(relx=1.0, rely=1.0, anchor="se", x=-25, y=-25)

window.mainloop()

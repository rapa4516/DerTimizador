import tkinter as tk
import os
from PIL import Image, ImageTk
from utils.util_services import execute_command
def on_click():
    execute_command()

# Criando a interface
janela = tk.Tk()
janela.title("Otimizador Black Desert (by ZXCASDQWEASDZXC)")
janela.geometry("680x402")
janela.resizable(False, False)

caminho_fundo = os.path.join("icons", "bg_main.png")
imagem_fundo_original = Image.open(caminho_fundo)
imagem_fundo_redimensionada = imagem_fundo_original.resize((680, 402))
imagem_fundo = ImageTk.PhotoImage(imagem_fundo_redimensionada)

fundo = tk.Label(janela, image=imagem_fundo, bg="#222229")
fundo.place(x=0, y=0, relwidth=1, relheight=1)

caminho_imagem = os.path.join("icons", "button_execute.png")
imagem_original = Image.open(caminho_imagem)
imagem_botao = ImageTk.PhotoImage(imagem_original)

# Criando o botão com a imagem
botao = tk.Button(
    janela,
    image=imagem_botao,
    command=on_click,
    bg="#1e1e1e",
    bd=0,
    activebackground="#1e1e1e"   
)

botao.image = imagem_botao  # previne coleta de lixo
botao.place(relx=1.0, rely=1.0, anchor="se", x=-25, y=-25)

janela.mainloop()
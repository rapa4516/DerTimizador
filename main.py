import tkinter as tk
import subprocess
import os
from PIL import Image, ImageTk  # <- ESSENCIAL para trabalhar com imagens

def executar_comandos():
    comandos = '''
    Write-Host "Executando comandos no PowerShell..."
    Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
    '''
    subprocess.run(["powershell", "-Command", comandos], shell=True)



# Criando a interface
janela = tk.Tk()
janela.title("ZXCASDQWEASDZXC")
janela.geometry("680x402")

caminho_fundo = os.path.join("icons", "bg_main.png")  # Substitua pelo nome do seu arquivo
imagem_fundo_original = Image.open(caminho_fundo)
imagem_fundo_redimensionada = imagem_fundo_original.resize((680, 402))  # Mesmo tamanho da janela
imagem_fundo = ImageTk.PhotoImage(imagem_fundo_redimensionada)

fundo = tk.Label(janela, image=imagem_fundo)
fundo.place(x=0, y=0, relwidth=1, relheight=1)

caminho_imagem = os.path.join("icons", "button_execute.png")
imagem_original = Image.open(caminho_imagem)
#imagem_redimensionada = imagem_original.resize((100, 100))
imagem_botao = ImageTk.PhotoImage(imagem_original)

# Criando o botão com a imagem
botao = tk.Button(
    janela,
    image=imagem_botao,
    command=executar_comandos,
    bg="#1e1e1e",
    bd=0,
    activebackground="#1e1e1e"
)
botao.image = imagem_botao  # previne coleta de lixo
botao.pack(pady=30)

janela.mainloop()
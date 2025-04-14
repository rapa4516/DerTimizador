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
janela.geometry("300x150")
janela.configure(bg="#1e1e1e")

# Carregando a imagem
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
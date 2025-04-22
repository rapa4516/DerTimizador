import subprocess
from tkinter import messagebox

def execute_command():

    STARTUP_TYPE_MAP = {
    "Automatic": 2,
    "Manual": 3,
    "Disabled": 4
    }

    servicos = {
        "AppIDSvc": "Manual",
        "AppXSvc": "Manual"
    }
    
    erros = []

    for nome, tipo in servicos.items():
        comando = f'Set-Service -Name "{nome}" -StartupType {tipo}'
        resultado = subprocess.run(["powershell", "-Command", comando], capture_output=True, text=True)

        if resultado.returncode == 0:
            messagebox.showinfo("Sucesso", f"\n{resultado.stderr}")
        elif:
            reg_path = fr"SYSTEM\CurrentControlSet\Services\{nome}"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE) as key:        
            winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, STARTUP_TYPE_MAP[startup_type])
            print(f"✔️ Serviço '{service_name}' alterado para '{startup_type}'.")
            
        if resultado.returncode != 0:
            erros.append(f"{nome}: {resultado.stderr.strip()}")

    return erros if erros else None

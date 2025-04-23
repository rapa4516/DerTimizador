import subprocess
import winreg
from tkinter import messagebox
from services.services import services

def execute_command():

    STARTUP_TYPE_MAP = {
    "Automatic": 2,
    "Manual": 3,
    "Disabled": 4
    }
    
    erros = []

    for serviceName, typeStartup in services.items():
        comando = f'Set-Service -Name "{serviceName}" -StartupType {typeStartup}'
        result = subprocess.run(["powershell", "-Command", comando], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"\n ✔️ {result.stderr} for {serviceName} in PowerShell" )
        else:
            print(f"\n ➖ {serviceName} declined in PowerShell")
            try:
                reg_path = fr"SYSTEM\CurrentControlSet\Services\{serviceName}"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, STARTUP_TYPE_MAP[typeStartup])
                print(f" ✔️ {serviceName}' for '{typeStartup}' in Regedit.")
            except Exception as e:
                erros.append(f"{serviceName}: Erro ao escrever no registro: {e}")
                print(f" ❌ '{serviceName}' for '{typeStartup}' in Regedit.")
                
    return erros if erros else None

import subprocess

def disk_clear():
    #subprocess.run(["cleanmgr.exe", "/sageset:1"])
    subprocess.run(["cleanmgr.exe", "/sagerun:1"])

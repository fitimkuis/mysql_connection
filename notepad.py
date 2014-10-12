import subprocess

def call_bat():
    p = subprocess.Popen('C:\\Users\\Timo\\Desktop\\notepad.bat', creationflags=subprocess.CREATE_NEW_CONSOLE)


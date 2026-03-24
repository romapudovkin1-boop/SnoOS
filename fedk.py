import subprocess
import os
subprocess.run("diskpart /s install.txt",shell=True)
disk = input("select a disk")
commands = [
    F"select disk {disk}"
    "\nclean" 
    "\ncreate partition efi size=512" 
    "\nformat quick fs=fat32"
    "\nassign letter N"
    "\ncreate partition primary"
    "\nformat quick fs=ntfs"
    "\nassign letter V"
]
path = input("введите путь к программе без имени программы И \\")
if path.endswith("\\"):
    path = input("введите путь к программе без имени программы")
# Создаем временный файл с командами
temp_script = "diskpart_script.txt"
with open(temp_script, "w") as f:
    for cmd in commands:
        f.write(cmd + "\n")
input(1)
subprocess.run("diskpart /s diskpart_script.txt")
os.system(f"dism /apply-image /imagefile={path}\\boot.wim /applydir=N:\\ /index:1")
os.system(f"dism /apply-image /imagefile={path}\\install.wim /applydir=V:\\ /index:1")
print("system will reboot in 5 seconds")
os.system("shutdown /r /f /t 5")


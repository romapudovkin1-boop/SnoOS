import subprocess
import os
import sys

subprocess.run("diskpart /s install.txt",shell=True)
disk = input("select a disk")
subprocess.run("diskpart /s install.txt",shell=True)
gpt = input("стоит ли у вашего диска в столбце GPT или дальше * ? Ответ да y ,нет n")
if gpt == "y":
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
if gpt == "n":
    commands = [
        F"select disk {disk}"
        "\n convert gpt"
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
fejdmr = input("WARNING! ALL data from the drive will be lost. press enter to continue. press n and enter to close the installer.")
if fejdmr == "n":
    sys.exit()
else:
    pass
subprocess.run("diskpart /s diskpart_script.txt")
os.system(f"dism /apply-image /imagefile={path}\\boot.wim /applydir=N:\\ /index:1")
os.system(f"dism /apply-image /imagefile={path}\\install.wim /applydir=V:\\ /index:1")
print("system will reboot in 5 seconds in UEFI select hackbgrt to boot")
os.system("shutdown /r /f /t 5")


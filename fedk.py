import os
import subprocess

try:
    # Использование shell=True
    result = subprocess.run(
        "diskpart /s listdisk.txt")
except subprocess.CalledProcessError as e:
    print(f"Ошибка выполнения: {e.stderr}")

disk = input("выберите диск")
partition = input("выберите раздел y - создать новый")
if partition == "y":
    os.system(f"diskpart&select disk {disk}&create partition primary")
size = input("выберите размер раздела в МБ минимум 32000 должно остаться 100 мб")
if size < 32000:
    size = 32000
os.system(
    f"diskpart&select disk {disk}&select partition {partition}&delete partition&create partition primary size={size}")
try:
    # Использование shell=True
    result = subprocess.run(
        "diskpart /s listdisk.txt")
except subprocess.CalledProcessError as e:
    print(f"Ошибка выполнения: {e.stderr}")
partition = input("выберите раздел ЕЩЁ РАЗ")
path = input("Введите путь к программе без имени файла и \ в конце")
try:
    # Использование shell=True
    result = subprocess.run(
        "diskpart /s listdisk.txt")
except subprocess.CalledProcessError as e:
    print(f"Ошибка выполнения: {e.stderr}")
efi = input("выберите 100 МБ РАЗДЕЛ efi (системный) только что созданный")
os.system(
        f'DISKPART&select disk {disk}&select partition {partition}&assign letter V&create partition EFI size=100&select partition {efi}&assign letter N&exit&dism /apply-image /imagefile:{path}\install.wim /applydir:V:\ /index:1&dism /apply-image /imagefile:{path}\\boot.wim& /applydir:V:\ /index:1')

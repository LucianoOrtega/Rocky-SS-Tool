# Rocky-SSTool
Rocky SS Tool es un programa escrito en Python con el fin de detectar hacks de Minecraft.

## Como se usa
Deben de poner en la misma carpeta donde esta el programa un archivo .txt llamado DPS,Java y Pcasvc, ahi pondran los dumps de Process Hacker 2, despues de eso abren el programa y esperan a que termine.
Es importante que no toquen ninguna tecla.

## Compilar proyecto

Solo basta con descargar PyInstaller (pip install pyinstaller), Colorama (pip install colorama) y escribir en siguiente comando:
pyinstaller main.py --onefile --ico="Rocky SSTool.ico"  --name="Rocky SSTool"

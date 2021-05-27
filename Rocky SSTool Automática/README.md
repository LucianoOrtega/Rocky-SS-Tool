# Rocky SSTool

Rocky SS Tool es un programa escrito en Python con el fin de detectar hacks de Minecraft. <br>

**Deteccion apartir de colores** <br>
*  **Color azul**<br>
Este es un archivo .zip, debes verificarlo, pero debería ser normal, algunas personas intentan bypassear los hacks en este tipo de archivos, así que por favor revise eso.
*  **Color rojo**<br>
Este es un .dll que es extremadamente extraño, el usuario podría estar usando NullDll o algo parecido. Revisar este archivo, Si no sabes como revisarlo recomiendo inyectarlo a java y fijarse que es lo que hace <br>
*  **Color amarillo** <br>
Este es un .exe, podría ser normal, pero debe verificarlo porque cabe la posibilidad que sea un external client,es recomendable que lo revise.

# Como se usa
Debes ejecutarlo como administrador con el minecraft abierto, Y empezara el analisis por si solo.

## Compilar proyecto

Solo basta con descargar tener python y las siguientes librerias: PyInstaller (pip install pyinstaller), Colorama (pip install colorama), psutil (pip install psutil), pathlib (pip install pathlib), requests(pip install requests) y escribir en siguiente comando:
pyinstaller main.py --onefile --ico="Rocky SSTool.ico" --name="Rocky SSTool" --uac-admin


# Nota importante
<br>
Si encuentra algún error, avíseme para que pueda arreglarlo. <br>
Gracias por leer, att: Luciano.

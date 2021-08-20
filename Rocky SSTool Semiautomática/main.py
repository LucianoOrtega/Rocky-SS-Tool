import msvcrt 
import base64
from colorama import init, Fore
from strings import dpsStrings, javawStrings, pcasvcStrings
init()

#Banner
print(Fore.GREEN + base64.b64decode( b'IC8kJCQkJCQkICAgICAgICAgICAgICAgICAgICAgIC8kJCAgICAgICAgICAgICAgICAgCnwgJCRfXyAgJCQgICAgICAgICAgICAgICAgICAgIHwgJCQgICAgICAgICAgICAgICAgIAp8ICQkICBcICQkICAvJCQkJCQkICAgLyQkJCQkJCR8ICQkICAgLyQkIC8kJCAgIC8kJCAKfCAkJCQkJCQkLyAvJCRfXyAgJCQgLyQkX19fX18vfCAkJCAgLyQkL3wgJCQgIHwgJCQgCnwgJCRfXyAgJCR8ICQkICBcICQkfCAkJCAgICAgIHwgJCQkJCQkLyB8ICQkICB8ICQkIAp8ICQkICBcICQkfCAkJCAgfCAkJHwgJCQgICAgICB8ICQkXyAgJCQgfCAkJCAgfCAkJCAKfCAkJCAgfCAkJHwgICQkJCQkJC98ICAkJCQkJCQkfCAkJCBcICAkJHwgICQkJCQkJCQgCnxfXy8gIHxfXy8gXF9fX19fXy8gIFxfX19fX19fL3xfXy8gIFxfXy8gXF9fX18gICQkIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC8kJCAgfCAkJCAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHwgICQkJCQkJC8gCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXF9fX19fXy8gIAogIC8kJCQkJCQgICAvJCQkJCQkICAvJCQkJCQkJCQgICAgICAgICAgICAgICAgICAvJCQKIC8kJF9fICAkJCAvJCRfXyAgJCR8X18gICQkX18vICAgICAgICAgICAgICAgICB8ICQkCnwgJCQgIFxfXy98ICQkICBcX18vICAgfCAkJCAgLyQkJCQkJCAgIC8kJCQkJCQgfCAkJAp8ICAkJCQkJCQgfCAgJCQkJCQkICAgIHwgJCQgLyQkX18gICQkIC8kJF9fICAkJHwgJCQKIFxfX19fICAkJCBcX19fXyAgJCQgICB8ICQkfCAkJCAgXCAkJHwgJCQgIFwgJCR8ICQkCiAvJCQgIFwgJCQgLyQkICBcICQkICAgfCAkJHwgJCQgIHwgJCR8ICQkICB8ICQkfCAkJAp8ICAkJCQkJCQvfCAgJCQkJCQkLyAgIHwgJCR8ICAkJCQkJCQvfCAgJCQkJCQkL3wgJCQKIFxfX19fX18vICBcX19fX19fLyAgICB8X18vIFxfX19fX18vICBcX19fX19fLyB8X18vCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg').decode() + "\nEl escaneo empezo, porfavor aguarde y no toque ninguna tecla.", end='')
#Banner
print("\n"+ Fore.LIGHTCYAN_EX+"-"*60)
for client in open('DPS.txt', 'r').read().splitlines():

    if ': ' in client and client.startswith('0x'):
        
        client = client[client.index(':') + 2:]

        for cheat, name in dpsStrings.items():

            if cheat in client:
                print(Fore.RED + f'{name} ({cheat}) fue encontrado en DPS.')

for client in open('Pcasvc.txt', 'r').read().splitlines():

    if ': ' in client and client.startswith('0x'):
        
        client = client[client.index(':') + 2:]

        for cheat, name in pcasvcStrings.items():

            if cheat in client:
                print(Fore.RED + f'{name} ({cheat}) fue encontrado en PcaSvc.')

for client in open('Java.txt', 'r').read().splitlines():

    if ': ' in client and client.startswith('0x'):
        
        client = client[client.index(':') + 2:]

        for cheat, name in javawStrings.items():

            if cheat in client:
                print(Fore.RED + f'{name} ({cheat}) fue encontrado en Java/Javaw.')


print(Fore.LIGHTCYAN_EX+"-"*28 + "Fin" + "-"*29)
print(Fore.RESET + "Cierre la ventana, ¡El análisis ya ha terminado!")
key = None
while key != '\x1b':
    key = msvcrt.getch()
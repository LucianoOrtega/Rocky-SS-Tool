import msvcrt #Evitar que se cierre el script 
import re #Buscar las string
import base64 #Banner
import colorama #Poner colores a los textos
from colorama import init, Fore, Back, Style #Poner colores a los textos
init()

# Anti Alt-F4

# Anti Alt-F4

#Abrir el texto y leerlo
textfile = open('Search results.txt', 'r')
filetext = textfile.read()
textfile.close()
#Abrir el texto y leerlo

#Banner
print(Fore.GREEN + base64.b64decode( b'IC8kJCQkJCQkICAgICAgICAgICAgICAgICAgICAgIC8kJCAgICAgICAgICAgICAgICAgCnwgJCRfXyAgJCQgICAgICAgICAgICAgICAgICAgIHwgJCQgICAgICAgICAgICAgICAgIAp8ICQkICBcICQkICAvJCQkJCQkICAgLyQkJCQkJCR8ICQkICAgLyQkIC8kJCAgIC8kJCAKfCAkJCQkJCQkLyAvJCRfXyAgJCQgLyQkX19fX18vfCAkJCAgLyQkL3wgJCQgIHwgJCQgCnwgJCRfXyAgJCR8ICQkICBcICQkfCAkJCAgICAgIHwgJCQkJCQkLyB8ICQkICB8ICQkIAp8ICQkICBcICQkfCAkJCAgfCAkJHwgJCQgICAgICB8ICQkXyAgJCQgfCAkJCAgfCAkJCAKfCAkJCAgfCAkJHwgICQkJCQkJC98ICAkJCQkJCQkfCAkJCBcICAkJHwgICQkJCQkJCQgCnxfXy8gIHxfXy8gXF9fX19fXy8gIFxfX19fX19fL3xfXy8gIFxfXy8gXF9fX18gICQkIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC8kJCAgfCAkJCAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHwgICQkJCQkJC8gCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXF9fX19fXy8gIAogIC8kJCQkJCQgICAvJCQkJCQkICAvJCQkJCQkJCQgICAgICAgICAgICAgICAgICAvJCQKIC8kJF9fICAkJCAvJCRfXyAgJCR8X18gICQkX18vICAgICAgICAgICAgICAgICB8ICQkCnwgJCQgIFxfXy98ICQkICBcX18vICAgfCAkJCAgLyQkJCQkJCAgIC8kJCQkJCQgfCAkJAp8ICAkJCQkJCQgfCAgJCQkJCQkICAgIHwgJCQgLyQkX18gICQkIC8kJF9fICAkJHwgJCQKIFxfX19fICAkJCBcX19fXyAgJCQgICB8ICQkfCAkJCAgXCAkJHwgJCQgIFwgJCR8ICQkCiAvJCQgIFwgJCQgLyQkICBcICQkICAgfCAkJHwgJCQgIHwgJCR8ICQkICB8ICQkfCAkJAp8ICAkJCQkJCQvfCAgJCQkJCQkLyAgIHwgJCR8ICAkJCQkJCQvfCAgJCQkJCQkL3wgJCQKIFxfX19fX18vICBcX19fX19fLyAgICB8X18vIFxfX19fX18vICBcX19fX19fLyB8X18vCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg').decode() + "\nEl escaneo empezo, porfavor aguarde y no toque ninguna tecla.", end='')
#Banner

#Strings 
itami20 = "!2020/09/28:01:13:10!0!"
itami14 = "!2016/01/20:08:28:11!27826f2!"
itami141 = "!2020/08/24:15:03:39"
itami13 = "!2020/07/21:00:58:02!0!"
itami = "20:02:41:42!0!"
itami2 = "!2020/08/25:23:53:56!0!"
koidnew = "!2020/07/22:23:28:56!0!"
koidold = "!2020/05/29:06:27:30!0!"
itori = "!2075/11/30:19:16:01!0!"
axenta = "!2079/02/13:00:40:14!0!"
ettlen = "!2019/11/08:00:11:02!0!"
mind = "!2041/10/08:08:07:41"
icetea = "!2020/02/02:18:48:40"
icetea2 = "02:18:48:40"
icetea3 = "21:15:49:58"
icetea4 = "22:18:37:28"
icetea5 = "24:06:33:40"
icetea6 = "24:15:18:47"
icetea7 = "26:03:27:09"
icetea8 = "23:19:38:33"
icetea9 = "22:07:12:31"
icetea10 = "22:05:58:43"
icetea11 = "13:06:37:22"
icetea12 = "09:00:55:22"
clientloader = "!2021/02/15:15:53:06!0!"
crypt = "2020/06/24:13:14:48!b40232!"
dragon1 = "2099/06/28:14"
dragon2 = "14:57:00!0!"
ectasy = "19:34:21!0!"
encephalon = "2083/04/22:21"
kuriumdps1 = "!2016/10/22:11:20:15!0!"
lean = "22:03:01:28!0!"
polaroid = "!2081/08/13:14:47:53!0!"
privileged = "19:19:01:21!0!"
SddsKB = "!2020/12/21:01:41:45!24b301!"
unicornnet = "!2076/05/18:04:53:15!0!"
vapeold = "!2016/10/26:20:57:40!0!"
vapelitecrack = "2019/05/19:20:48:16!751b9d52!"
vapev4 = "05:01:42:25!79961d"
vape2v4 = "!79d4e5!"
vertigolite = "07:09:19:51!0!"
wannacry = "2021/01/26:18:28:16!293402!"
zoomin1 = "!2021/03/01:18:39:50!0!"
zoomin2 = "!2021/03/04:19:12:37!0!"
zoomin3 = "!2021/03/06:09:27:18!0!"
zoomin4 = "!2021/03/09:18:51:00!0!"
zoomin5 = "!2021/03/09:19:32:42!0!"
#Strings

#Buscar las strings en el archivo e imprimirlas
matches = re.findall(r'\w*!2021/03/09:19:32:42!0!\w*' , filetext) + re.findall(r'\w*!2021/03/09:18:51:00!0!\w*' , filetext) + re.findall(r'\w*!2021/03/06:09:27:18!0!\w*' , filetext) + re.findall(r'\w*!2081/08/13:14:47:53!0!\w*' , filetext) + re.findall(r'\w*19:19:01:21!0!\w*' , filetext) + re.findall(r'\w*!2020/12/21:01:41:45!24b301!\w*' , filetext) + re.findall(r'\w*07:09:19:51!0!\w*' , filetext) + re.findall(r'\w*2021/01/26:18:28:16!293402!\w*' , filetext) + re.findall(r'\w*!2021/03/01:18:39:50!0!\w*' , filetext) + re.findall(r'\w*!2021/03/04:19:12:37!0!\w*' , filetext) + re.findall(r'\w*05:01:42:25!79961d\w*' , filetext) + re.findall(r'\w*2019/05/19:20:48:16!751b9d52!\w*' , filetext) + re.findall(r'\w*!2016/10/26:20:57:40!0!\w*' , filetext) + re.findall(r'\w*!2076/05/18:04:53:15!0!\w*' , filetext) + re.findall(r'\w*!2020/12/21:01:41:45!24b301!\w*' , filetext) + re.findall(r'\w*22:03:01:28!0!\w*' , filetext) + re.findall(r'\w*!2016/10/22:11:20:15!0!\w*' , filetext) + re.findall(r'\w*!2020/08/25:23:53:56!0!\w*' , filetext) + re.findall(r'\w*20:02:41:42!0!\w*' , filetext) + re.findall(r'\w*22:18:37:28\w*' , filetext) + re.findall(r'\w*24:06:33:40\w*' , filetext) + re.findall(r'\w*24:15:18:47\w*' , filetext) + re.findall(r'\w*26:03:27:09\w*' , filetext) + re.findall(r'\w*23:19:38:33\w*' , filetext) + re.findall(r'\w*22:07:12:31\w*' , filetext) + re.findall(r'\w*22:05:58:43\w*' , filetext) + re.findall(r'\w*13:06:37:22\w*' , filetext) + re.findall(r'\w*09:00:55:22\w*' , filetext) + re.findall(r'\w*02:18:48:40\w*' , filetext) + re.findall(r'\w*21:15:49:58\w*' , filetext) + re.findall(r'\w*2083/04/22:21\w*' , filetext) + re.findall(r'\w*19:34:21!0!\w*' , filetext) + re.findall(r'\w*14:57:00!0!\w*' , filetext) + re.findall(r'\w*2099/06/28:14\w*' , filetext) + re.findall(r'\w*2020/06/24:13:14:48!b40232!\w*' , filetext) + re.findall(r'\w*!2021/02/15:15:53:06!0!\w*' , filetext) + re.findall(r'\w*!2020/09/28:01:13:10!0!\w*' , filetext) + re.findall(r'\w*!2016/01/20:08:28:11!27826f2!\w*', filetext) + re.findall(r'\w*!2020/08/24:15:03:39\w*', filetext) + re.findall(r'\w*!!2020/07/21:00:58:02!0!\w*', filetext)+ re.findall(r'\w*!2020/05/29:06:27:30!0!\w*', filetext) + re.findall(r'\w*!2075/11/30:19:16:01!0!\w*', filetext)+ re.findall(r'\w*!2079/02/13:00:40:14!0!\w*', filetext) + re.findall(r'\w*!2019/11/08:00:11:02!0!\w*', filetext) + re.findall(r'\w*!2041/10/08:08:07:41\w*', filetext) + re.findall(r'\w*!2020/02/02:18:48:40\w*', filetext) + re.findall(r'\w*!2020/07/22:23:28:56!0!\w*', filetext)
StringsEncontradas = "".join(matches)
print ( )
print ( )
print ( )
#Buscar las strings en el archivo e imprimirlas

#Imprimir el hack encontrado
if itami20 in StringsEncontradas:
    print(Style.BRIGHT + Fore.RED + "Itami 2.3 encontrado!") 

if itami14 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Itami 1.4 encontrado!")

if itami141 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Itami 1.4.1 encontrado!")

if itami13 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Itami 1.3 encontrado!")

if itami in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Itami Client encontrado!")

if itami2 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Itami Client encontrado!")

if koidnew in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Koid Client encontrado!")

if koidold in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Koid Client encontrado!")

if itori in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Itori 2.0 encontrado!")

if axenta in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Axenta Autoclicker encontrado!")

if ettlen in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Ettlen Client encontrado!")

if mind in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Mind Client encontrado!")

if icetea in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado")

if icetea2 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if icetea3 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if icetea4 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if icetea5 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if icetea6 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if icetea7 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if icetea8 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if icetea9 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if icetea10 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if icetea11 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if icetea12 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Icetea Client encotrado!")

if clientloader in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Client Loader encontrado!")

if crypt in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Crypt Client encontrado!")

if dragon1 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Dragon Client encontrado!")

if dragon2 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Dragon Client encontrado!")

if ectasy in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Ectasy Client encontrado!")

if encephalon in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Encephalon Client encontrado!")

if kuriumdps1 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Kurium Client encontrado!")

if lean in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Lean Client encontrado!")

if polaroid in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Polaroid Client encontrado!")

if privileged in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Privileged Client encontrado!")

if SddsKB in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "SddsKB Client encontrado!")

if unicornnet in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Unicorn NET encontrado!")

if vapeold in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Vape (Old) encontrado!")

if vapelitecrack in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Vape Lite Crack encontrado!")

if vapev4 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Vape V4 encontrado!")

if vape2v4 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Vape V4 encontrado!")

if vertigolite in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Vertigo Lite encontrado!")

if wannacry in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "WannaCry Client encontrado!")

if zoomin1 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Zoomin Client encontrado!")

if zoomin2 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Zoomin Client encontrado!")

if zoomin3 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Zoomin Client encontrado!")

if zoomin4 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Zoomin Client encontrado!")

if zoomin5 in StringsEncontradas:
    print (Style.BRIGHT + Fore.RED + "Zoomin Client encontrado!")

#Imprimir el hack encontrado

#Imprimir todas las strings de hacks encontradas
print (Fore.WHITE + "")
print ('Todas las strings encontradas:')
print ("")
print(matches)
#Imprimir todas las strings de hacks encontradas
        
print ("")

print("Cierre la ventana, ¡El analisis ya ha terminado!")
key = None
while key != '\x1b':
    key = msvcrt.getch()
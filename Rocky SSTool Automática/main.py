import psutil
import subprocess
import colorama
import os
import sys
import time
import zipfile
import base64
import msvcrt
import requests
from strings import javawStrings, dpsStrings, pcasvcStrings

class RockySSTool(object):

    url = 'https://github.com/glmcdona/strings2/raw/master/x64/Release/strings.exe'
    myfile = requests.get(url)
    open('C:/Windows/Temp/string.exe', 'wb').write(myfile.content)

    def __init__(self):
        self.recordingSoftwares = {"bdcam":"Bandicam", "action":"Action", "obs64":"OBS", "dxtory":"Dxtory", "nvidia share":"Geforce Experience", "camtasia":"Camtasia", "fraps":"Fraps", "screencast":"Screencast"}
        self.max_modification_time = 5
        self.path_with_username = '/'.join(os.getcwd().split('\\', 3)[:3])
        self.drive_letter = os.getcwd().split('\\', 1)[0]+'/'
        #Colores
        self.color_blue = colorama.Fore.BLUE
        self.color_red = colorama.Fore.RED
        self.color_green = colorama.Fore.GREEN
        self.color_magneta = colorama.Fore.LIGHTMAGENTA_EX
        self.color_yellow = colorama.Fore.YELLOW
        self.color_clear = colorama.Style.RESET_ALL
        self.welcome_message = colorama.Fore.GREEN + base64.b64decode( b'IC8kJCQkJCQkICAgICAgICAgICAgICAgICAgICAgIC8kJCAgICAgICAgICAgICAgICAgCnwgJCRfXyAgJCQgICAgICAgICAgICAgICAgICAgIHwgJCQgICAgICAgICAgICAgICAgIAp8ICQkICBcICQkICAvJCQkJCQkICAgLyQkJCQkJCR8ICQkICAgLyQkIC8kJCAgIC8kJCAKfCAkJCQkJCQkLyAvJCRfXyAgJCQgLyQkX19fX18vfCAkJCAgLyQkL3wgJCQgIHwgJCQgCnwgJCRfXyAgJCR8ICQkICBcICQkfCAkJCAgICAgIHwgJCQkJCQkLyB8ICQkICB8ICQkIAp8ICQkICBcICQkfCAkJCAgfCAkJHwgJCQgICAgICB8ICQkXyAgJCQgfCAkJCAgfCAkJCAKfCAkJCAgfCAkJHwgICQkJCQkJC98ICAkJCQkJCQkfCAkJCBcICAkJHwgICQkJCQkJCQgCnxfXy8gIHxfXy8gXF9fX19fXy8gIFxfX19fX19fL3xfXy8gIFxfXy8gXF9fX18gICQkIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC8kJCAgfCAkJCAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHwgICQkJCQkJC8gCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXF9fX19fXy8gIAogIC8kJCQkJCQgICAvJCQkJCQkICAvJCQkJCQkJCQgICAgICAgICAgICAgICAgICAvJCQKIC8kJF9fICAkJCAvJCRfXyAgJCR8X18gICQkX18vICAgICAgICAgICAgICAgICB8ICQkCnwgJCQgIFxfXy98ICQkICBcX18vICAgfCAkJCAgLyQkJCQkJCAgIC8kJCQkJCQgfCAkJAp8ICAkJCQkJCQgfCAgJCQkJCQkICAgIHwgJCQgLyQkX18gICQkIC8kJF9fICAkJHwgJCQKIFxfX19fICAkJCBcX19fXyAgJCQgICB8ICQkfCAkJCAgXCAkJHwgJCQgIFwgJCR8ICQkCiAvJCQgIFwgJCQgLyQkICBcICQkICAgfCAkJHwgJCQgIHwgJCR8ICQkICB8ICQkfCAkJAp8ICAkJCQkJCQvfCAgJCQkJCQkLyAgIHwgJCR8ICAkJCQkJCQvfCAgJCQkJCQkL3wgJCQKIFxfX19fX18vICBcX19fX19fLyAgICB8X18vIFxfX19fX18vICBcX19fX19fLyB8X18vCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg').decode() +colorama.Style.RESET_ALL
        self.end_message = colorama.Fore.LIGHTCYAN_EX+"-"*28 + "Fin" + "-"*29+colorama.Style.RESET_ALL
        self.separator = colorama.Fore.LIGHTCYAN_EX+"-"*60 +self.color_clear

        if sys.platform == "win32":
            self.minecraft_path = self.path_with_username + "/AppData/Roaming/.minecraft"
            self.clear_command = os.system('cls')

    def get_service_pid(self,name,is_csrss):
        if is_csrss:
            return [proc.pid for proc in psutil.process_iter() if proc.name() == "csrss.exe"]
        response = str(subprocess.check_output(f'tasklist /svc /FI "Services eq {name}"')).split('\\r\\n')
        for process in response:
            if name in process:
                pid = process.split()[1]
                return pid

    def minecraft_abierto(self):
        for p in psutil.process_iter(attrs=['pid', 'name']):
            if 'javaw' in p.info['name']:  
                pid = p.info['pid']
                process = p.cmdline()
                mcprocess_info = {}
                for argument in process:
                    if "--" in argument:
                        mcprocess_info[argument.split("--")[1]] = process[process.index(argument) + 1]
                if "version" in mcprocess_info:
                    print(self.color_magneta+"Minecraft encontrado, buscando información..."+self.color_clear)
                    self.javawPid = pid
                    if "username" in mcprocess_info:
                        print(f'    Username: {mcprocess_info["username"]}')
                    else: print("    No se pudo obtener el nombre del usuario")
                    print(f'    Version: {mcprocess_info["version"]}')
                    print(f'    Path: {mcprocess_info["gameDir"]}')
                    return True
            elif 'java' in p.info['name']:
                 pid = p.info['pid']
                 process = p.cmdline()
                 mcprocess_info = {}
                 for argument in process:
                    if "--" in argument:
                        mcprocess_info[argument.split("--")[1]] = process[process.index(argument) + 1]
                 if "version" in mcprocess_info:
                    print(self.color_magneta+"Minecraft encontrado, buscando información..."+self.color_clear)
                    self.javawPid = pid
                    if "username" in mcprocess_info:
                        print(f'    Username: {mcprocess_info["username"]}')
                    print(f'    Version: {mcprocess_info["version"]}')
                    print(f'    Path: {mcprocess_info["gameDir"]}')
                    return True

        print(self.color_red+"El proceso Java/Javaw no fue encontrado"+self.color_clear)
        os.remove('C:\Windows\Temp\string.exe')
        print(self.color_red+"¡Cierre esta ventana y ejecute Minecraft!")
        key = None
        while key != '\x1b':
         key = msvcrt.getch()
        return False

        
    def common_hacks(self):
        if "huzuni" in os.listdir(self.minecraft_path): print(self.color_red+'Huzuni encontrado en la .minecraft'+self.color_clear)
        elif "Wurst" in os.listdir(self.minecraft_path): print(self.color_red+'Wurst encontrado en la .minecraft'+self.color_clear)
        elif "Impact" in os.listdir(self.minecraft_path): print(self.color_red+'Impact fue encontrado en la .minecraft'+self.color_clear)
        elif "Sigma5" in os.listdir(self.minecraft_path): print(self.color_red+'Sigma fue encontrado en la .minecraft'+self.color_clear)
        elif "Sigma" in os.listdir(self.minecraft_path): print(self.color_red+'Sigma fue encontrado en la .minecraft'+self.color_clear)
        elif "Wolfram" in os.listdir(self.minecraft_path): print(self.color_red+'Wolfram fue encontrado en la .minecraft'+self.color_clear)
        elif "Flux" in os.listdir(self.minecraft_path): print(self.color_red+'Flux fue encontrado en la .minecraft'+self.color_clear)
        elif "Aristois" in os.listdir(self.minecraft_path): print(self.color_red+'Aristois fue encontrado en la .minecraft'+self.color_clear)
        else: print(self.color_green+'Ningún cheat común encontrado en la .minecraft'+self.color_clear)
        
    def software_grabar(self):
        tasks = str(subprocess.check_output('tasklist')).lower()
        found = [x for x in self.recordingSoftwares if x in tasks]
        if found:
            print(self.color_red+'Software(s) de grabación encontrado(s)'+self.color_clear)
            for software in found:
                print(f'    {self.color_yellow}{self.recordingSoftwares[software]}{self.color_clear} encontrado')
        else:
            print(self.color_green+'No se ha encontrado ningún software de grabación'+self.color_clear)

    def modification_time(self):
        print(self.color_magneta+'Fecha de modificación de las carpetas principales'+self.color_clear)
        #RecycleBin
        recycle_bin_path = self.drive_letter+"/$Recycle.Bin/"
        modTime = os.path.getmtime(recycle_bin_path)
        modTime = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(modTime)).split(' ')
        print(f'    Recycle Bin: {modTime[1]} {modTime[0]}')

        #Mods
        if os.path.isdir(self.minecraft_path + "/mods"):
         mods_path = self.minecraft_path + "/mods"
         modTime = os.path.getmtime(mods_path)
         modTime = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(modTime)).split(' ')
         print(f'    Mods: {modTime[1]} {modTime[0]}')

        #Versions
        mods_path = self.minecraft_path + "/versions"
        modTime = os.path.getmtime(mods_path)
        modTime = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(modTime)).split(' ')
        print(f'    Versions: {modTime[1]} {modTime[0]}')

        #Texturepacks
        mods_path = self.minecraft_path + "/resourcepacks"
        modTime = os.path.getmtime(mods_path)
        modTime = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(modTime)).split(' ')
        print(f'    Resourcepacks: {modTime[1]} {modTime[0]}')

    def show_jar_classes(self,jar_file):
        try:
            zf = zipfile.ZipFile(jar_file, 'r')
        except:
            return []
        all_classes = []
        try:
            lst = zf.infolist()
            for zi in lst:
                fn = zi.filename
                if fn.endswith('.class'):
                    all_classes.append(fn.split('/')[len(fn.split('/'))-1])
        finally:
            zf.close()
        return all_classes

    def is_raven(self,zip_to_check):
        try:
            zf = zipfile.ZipFile(zip_to_check, 'r')
            mcmodinfo = dict(json.load(zf.open('mcmod.info'))[0])
            if mcmodinfo['authorList'] == ['OFP', 'Fyu', 'spiderfrog', 'Yario & Extazz'] and mcmodinfo['url'] == 'https://www.youtube.com/ofpmedia': return True
        except: 
            pass
        return False

    def mods(self):
        print(self.color_magneta+'Aquí tienes una lista de todos los mods'+self.color_clear)
        path = self.minecraft_path + "/mods"
        path2 = self.minecraft_path + "/mods/1.8.9"
        path3 = self.minecraft_path + "/mods/1.7.10"
        path4 = self.minecraft_path + "/mods/1.7"

        if os.path.isdir(self.minecraft_path + "\mods"):
         for x in os.listdir(path): 
            if x.endswith('.jar'):
                if "$ . class" in self.show_jar_classes(self.minecraft_path + "/mods"+x): print(self.color_red + x + " (Injected)"+ self.color_clear)
                elif "  ‏ $ ‏‏ .class" in self.show_jar_classes(self.minecraft_path + "/mods"+x):print(self.color_red + x + " (Injected)"+ self.color_clear) 
                else: print(self.color_green + x + self.color_clear)
            elif x.endswith('zip'):
                if self.is_raven(self.minecraft_path + "/mods"+x): print(self.color_red + x + " Raven Ghost Client encontrado!"+ self.color_clear)
                else: print(self.color_yellow + x + self.color_clear)

        if os.path.isdir(self.minecraft_path + "/mods/1.8.9"):
         for x in os.listdir(path2): 
            if x.endswith('.jar'):
                if "$ . class" in self.show_jar_classes(self.minecraft_path + "/mods/1.8.9/"+x): print(self.color_red + x + " (Injected)"+ self.color_clear)
                elif "  ‏ $ ‏‏ .class" in self.show_jar_classes(self.minecraft_path + "/mods/1.8.9/"+x):print(self.color_red + x + " (Injected)"+ self.color_clear) 
                else: print(self.color_green + x + self.color_clear)
            elif x.endswith('zip'):
                if self.is_raven(self.minecraft_path + "/mods/1.8.9/"+x): print(self.color_red + x + " Raven Ghost Client encontrado!"+ self.color_clear)
                else: print(self.color_yellow + x + self.color_clear)

        if os.path.isdir(self.minecraft_path + "/mods/1.7.10"):
         for x in os.listdir(path3): 
          if x.endswith('.jar'):
            if "$ . class" in self.show_jar_classes(self.minecraft_path + "/mods/1.7.10/"+x): print(self.color_red + x + " (Injected)"+ self.color_clear)
            elif "  ‏ $ ‏‏ .class" in self.show_jar_classes(self.minecraft_path + "/mods/1.7.10/"+x):print(self.color_red + x + " (Injected)"+ self.color_clear) 
            else: print(self.color_green + x + self.color_clear)
          elif x.endswith('zip'):
                if self.is_raven(self.minecraft_path + "/mods/1.7.10/"+x): print(self.color_red + x + " Raven Ghost Client encontrado!"+ self.color_clear)
                else: print(self.color_yellow + x + self.color_clear)

        if os.path.isdir(self.minecraft_path + "/mods/1.7"):
         for x in os.listdir(path4): 
          if x.endswith('.jar'):
            if "$ . class" in self.show_jar_classes(self.minecraft_path + "/mods/1.7/"+x): print(self.color_red + x + " (Injected)"+ self.color_clear)
            elif "  ‏ $ ‏‏ .class" in self.show_jar_classes(self.minecraft_path + "/mods/1.7/"+x):print(self.color_red + x + " (Injected)"+ self.color_clear) 
            else: print(self.color_green + x + self.color_clear)
          elif x.endswith('zip'):
                if self.is_raven(self.minecraft_path + "/mods/1.7/"+x): print(self.color_red + x + " Raven Ghost Client encontrado!"+ self.color_clear)
                else: print(self.color_yellow + x + self.color_clear)


    def get_strings(self,PID):
        cmd = f'string.exe -pid {PID} -raw -nh'
        os.chdir(os.path.abspath("C:\Windows\Temp"))
        strings = str(subprocess.check_output(cmd)).replace("\\\\","/")
        strings = list(set(strings.split("\\r\\n")))
        return strings

    def check_strings(self):
        print(self.color_magneta+'Comprobando strings... (esto puede tardar un rato)'+self.color_clear)
        #Check javaw
        javaw_strings = self.get_strings(self.javawPid)
        found = [f'{javawStrings[x]} ({x})' for x in javaw_strings if x in javawStrings]

        if found:
            for hack in found:
                print(self.color_red+f'    {hack} fue encontrado en Javaw'+self.color_clear)
        else:
            print(self.color_green+f'    Ningún cheat fue encontrado Javaw'+self.color_clear)

        #Check Pcasvc
        pcasvcPid = self.get_service_pid('PcaSvc', False)        
        pcasvc_strings = self.get_strings(pcasvcPid)
        found = [f'{pcasvcStrings[x]} ({x})' for x in pcasvc_strings if x in pcasvcStrings]

        if found:
            for hack in found:
                print(self.color_red+f'    {hack} fue encontrado en PcaSvc'+self.color_clear)
        else:
            print(self.color_green+f'    Ningún cheat fue encontrado en PcaSvc'+self.color_clear)

        #Check dps
        dpsPid = self.get_service_pid('DPS', False)
        dps_strings = self.get_strings(dpsPid)
        dps_strings = ['.exe!'+x.split('!')[3] for x in dps_strings if '.exe!' in x and x.startswith('!!')]

        found = [x for x in dps_strings if x in dpsStrings]
        if found:
            for string in found: print(self.color_red+f'    {dpsStrings[string]} ({string}) fue encontrado en DPS'+self.color_clear)
        else:
            print(self.color_green+f'    Ningún cheat fue encontrado en DPS'+self.color_clear)
        
    def recents(self):
            print(self.color_magneta+"He encontrado los siguientes archivos recientes"+self.color_clear)
            path = self.path_with_username + "/AppData/Roaming/Microsoft/Windows/Recent/"
            for e in os.listdir(path):
                e = e.replace('.lnk','')
                if e.endswith('.zip'): print(e.replace('.zip', '') + self.color_blue + ".zip"+ self.color_clear)
                elif e.endswith('.dll'): print(e.replace('.dll', '') + self.color_red + ".dll"+ self.color_clear)
                elif e.endswith('exe'): print(e.replace('.exe', '') + self.color_yellow + ".exe"+ self.color_clear)

    def downloads(self):
        path = self.path_with_username + "/Downloads/"
        print(self.color_magneta+"He encontrado los siguientes archivos en descargas"+self.color_clear)
        for e in os.listdir(path):
            e = e.replace('.lnk','')
            if e.endswith('.zip'): print(e.replace('.zip', '') + self.color_blue + ".zip"+ self.color_clear)
            elif e.endswith('.dll'): print(e.replace('.dll', '') + self.color_red + ".dll"+ self.color_clear)
            elif e.endswith('.exe'): print(e.replace('.exe', '') + self.color_yellow + ".exe"+ self.color_clear)

    def deleteTemp(self):
     os.remove('C:\Windows\Temp\string.exe')
            

ss = RockySSTool()

ss.clear_command
print(ss.welcome_message)
if ss.minecraft_abierto() == True:
    print(ss.separator)
    ss.common_hacks()
    print(ss.separator)
    ss.software_grabar()
    print(ss.separator)
    ss.mods()
    print(ss.separator)
    ss.modification_time()
    print(ss.separator)
    ss.check_strings()
    print(ss.separator)
    ss.recents()
    print(ss.separator)
    ss.downloads()
    ss.deleteTemp()

print(ss.end_message)

print("Cierre la ventana, ¡El análisis ya ha terminado!")
key = None
while key != '\x1b':
    key = msvcrt.getch()

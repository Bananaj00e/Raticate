import  os
import time
import random
from colorama import Fore, Back, Style
import urllib.request
from progress.bar import Bar





def updatetermux() :
         print (Fore.GREEN + "[*] Updating")
         time.sleep(3)
         os.system("rm -r /data/data/com.termux/files/usr/share/Pikachu")
         os.system("cd /data/data/com.termux/files/usr/share")
         os.system("git clone")

def updatelinux() :
         print (Fore.GREEN + "[*] Updating")
         time.sleep(3)
         os.system("rm -r /usr/share/Pikachu")
         os.system("cd /usr/share")
         os.system("git clone ")
         os.system("clear")




update = ("1.0")
url = ("http://wiressouls.c1.biz/update.txt")



############################################  Update #################################################
web = urllib.request.urlopen(url)
x = (web.read().decode())
print(x)

os.system("clear")
bar = Bar(Fore.LIGHTYELLOW_EX + '[*] Checking For Updates', max=100)
for i in range(100):
    time.sleep(0.03)

    bar.next()
bar.finish()

if x > update:
    time.sleep(4)
    print(Fore.GREEN + "[*] Update Found")
    time.sleep(4)

    os.system("clear")

    print(Fore.LIGHTYELLOW_EX + """


 (\__/)   -----------------
 (='.')   | Do you want to  |
 (_(")(") |     Update ?    |
        |  |                 |
          | (y) Yes (n) No  |
          -----------------
 """)
    update = input("[Update] > ")
    if update == "y":
####update####
      print (Fore.GREEN + "    Linux        Termux")
      print (Fore.GREEN + "     (1)          (2) ")
  
      ver = input (" >  ")
      if ver == "1" :
         updatelinux()
      elif ver == "2" :
         updatetermux()

else:
    time.sleep(4)
    print(Fore.RED + "[*] No Update Found")
    time.sleep(4)
    os.system("clear")



################################################### Running #######################################################

time.sleep(3)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu |")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu |")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu |")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu |")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu /")
time.sleep(0.5)
time.sleep(2)
os.system("clear")
print(Fore.LIGHTYELLOW_EX + "[*] Welcome To Pikatchu")
time.sleep(2.5)
os.system("clear")
##################################################" Pikatcu ############################################################

############### Random Logo ################







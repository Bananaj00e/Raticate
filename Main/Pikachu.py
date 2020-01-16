try:
 import  os
 import time
 import random
 from colorama import Fore, Back, Style
 import urllib.request
 from progress.bar import Bar

except ImportError as e :
 os.system("clear")
 print (Fore.RED + "[*] a Module Has Not Installed")
 time.sleep(3)
 os.system("clear")
 print (Fore.GREEN + "[*] Installing ")
 time.sleep(4)
 os.system("clear")
 os.system("pip3 install urllib")
 os.system("pip3 install progress.bar")
 os.system("pip3 install progress")
 os.system("clear")

import  os
import time
import random
from colorama import Fore, Back, Style
import urllib.request
from progress.bar import Bar





def updatetermux() :
         print (Fore.GREEN + "[*] Updating")
         time.sleep(3)
         os.system("rm -rf /data/data/com.termux/files/usr/share/Pikachu")
         os.system("cd /data/data/com.termux/files/usr/share")
         os.system("git clone https://github.com/Bananaj00e/Pikachu.git")
         os.system("clear")

def updatelinux() :
         print (Fore.GREEN + "[*] Updating")
         time.sleep(3)
         os.system("rm -rf /usr/share/Pikachu")
         os.system("cd /usr/share")
         os.system("git clone https://github.com/Bananaj00e/Pikachu.git ")
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


foo = ['2','1','3']
random = (random.choice(foo))



if random == "1" :

 print (Fore.LIGHTYELLOW_EX + """
Pikachu! : This Is My Real Password

V              V              V              V              V
OIWEQPOISDFBKJFOIWEQPOISDFBKJFOIWEQPOISDFBKJFOIWEQPOISDFBKJF
EDGHOUIEROUIYWEVDGHOXUIEROIYWEVDGHEOXUIEOIYWEVDGHEOXUIEOIYWE
KJBSVDBOIWERTBAKJBSVEDBOIWRTBAKJBSOVEDBOWRTBAKJBSOVEDBOWRTBA
SFDHNWECTBYUVRGSFDHNYWECTBUVRGSFDHCNYWECBUVRGSFDHCNYWECBUVRG
HNOWFHLSFDGWVRGHNOWFGHLSFDWVRGHNOWSFGHLSDWVRGHNLOWSFGLSDWVRG
YPOWVXTNWFECHRGYPOWVEXTNWFCHRGYPOWNVEXTNFCHRGYPWOWNVETNFCHRG
SVYUWXRGTWVETUISVYUWVXRGTWVETUISVYUWVXRGWVETUISVYUWVXRGWVETU
WVERBYOIAWEYUIVWVERBEYOIAWEYUIVWVERBEYOIWEYUIVWLVERBEOIWEYUI
EUIOETOUINWEBYOEUIOEWTOUINWEBYOEUIOEWTOUNWEBYOETUIOEWOUNWEBY
WFVEWVETN9PUW4TWFVEWPVETN9UW4TWFVETWPVET9UW4TWFBVETWPET9UW4T
NOUWQERFECHIBYWNOUWQXERFECIBYWNOUWFQXERFCIBYWNOFUWFQXRFCIBYW
VEHWETUQECRFVE[VEHWERTUQECFVE[VEHWQERTUQCFVE[VEOHWQERUQCFVE[
UIWTUIRTWUYWQCRUIWTUYIRTWUWQCRUIWTXUYIRTUWQCRUIBWTXUYRTUWQCR
IYPOWOXNPWTHIECIYPOWTOXNPWHIECIYPONWTOXNWHIECIYLPONWTXNWHIEC
R9UHWVETPUNRQYBR9UHWVETPUNRQYBR9UHWVETPUNRQYBR9UHWVETPUNRQYB
X              X              X              X              X






  """)


elif random == ("2") :
 print ("""

           //
         _//
        .. ~~-_     <==== You
   ___m<___m___~.___
   _|__|__|__|__|___|
   |__|__|__|__|__|_
    |_ |__|__|_|__|_|     <===== FireWall
   |__|__|__|_|__|__|
   ()))()()()())()())



  """)

elif random == ("3") :
 print ("""

  //
 (")
 UU\    Little White Rabbit
 <><>*

---------------------------------------------

 """)


##########################Pikachu##########################


def Start() :

 commandd = input (Fore.LIGHTYELLOW_EX + "[Pikachu] >")


 if commandd == ("clear") :
  os.system("clear")
  Start()

 elif commandd == ("exit") :
  print (Fore.GREEN + "[*] Bye Bye :( ")

 elif commandd == ("help") :
  print(Fore.GREEN + """
+
  ________________+ +
 |   Help Menu    |
 |----------------|____
+| show  | Show Modules|  +
 | use   | use Modules |
 | clear | Clear Screen|  +
 | exit  | Exit Pukachu|
 | update|  For Update |
  ---------------------
+     +       +        +   +
+ +             +    +
  """)
  Start()

 elif commandd == ("update") :
  print (Fore.GREEN + "    Linux        Termux")
  print (Fore.GREEN + "     (1)          (2) ")
  ver = input (" >  ")
  if ver == "1" :
         updatelinux()
  elif ver == "2" :
         updatetermux()


#########################Modules#####################


 elif commandd == ("show") :


  print (Fore.GREEN + """
          Exploits
 ---------------------------






           Scanner
 ---------------------------






             Post
 ----------------------------






             Hash
 ----------------------------








   """)
  Start()






######################################################
 else :
  print (Fore.RED + "[*] error")
  Start()









Start()

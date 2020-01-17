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





def update() :
         print (Fore.GREEN + "[*] Updating")
         time.sleep(3)
         os.system("rm -rf ~/../usr/share/Pikachu")
         os.system("git clone https://github.com/Bananaj00e/Pikachu.git ~/../usr/share/Pikachu")
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
time.sleep(2)
print (Fore.GREEN + "[*] Current Version : ",update)
time.sleep(2)
print (Fore.GREEN + "[*] Last Version : ",x)


if x > update:
    time.sleep(4)
    print(Fore.GREEN + "[*] Update Found")
    time.sleep(4)

    os.system("clear")

    print(Fore.LIGHTYELLOW_EX + """


 (\__/)    -----------------
 (='.')   | Do you want to  |
 (_(")(") |     Update ?    |
          |                 |
          | (y) Yes (n) No  |
           -----------------
 """)
    update = input("[Update] > ")
    if update == "y":
####update####
      update()

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

foo = ['2','3']
random = random.choice(foo)





if random == ("2") :
 print ("""


         __
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
 | clear | Clear Screen|  +      +
 | exit  | Exit Pikachu| +
 | update|  For Update |
  ---------------------
+     +       +        +   +
+ +             +    +
  """)
  Start()

 elif commandd == ("update") :
  update = ("0.5")
  url = ("http://wiressouls.c1.biz/update.txt")
  ############################################  Update ######################################>
  web = urllib.request.urlopen(url)
  x = (web.read().decode())
  print ("The current version : ",update)
  print ("The current version : ",x)
  if update < x :
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

          Exploits                                    Rank                   Descrption
 ---------------------------






           Scanner
 ---------------------------






             Post
 ----------------------------
     pikachu/post/openssh/ssh_user_enum                Normal         in Openssh 7.2 you can enumerate users
     pikachu/post/wordpress/wordpress_user_enum        Good           in wordpress you can enumetate users




             Hash
 ----------------------------








   """)
  Start()

 elif commandd == ("use pikachu/post/openssh/ssh_user_enum") :
    os.system("clear") 
    print("""


                            Username Enumration Openssh
                                                         1.0



     """)
    os.system("bash ~/../usr/share/Pikachu/modules/post/openssh/ssh_user_enum/ssh_enum.sh")
    Start()
 elif commandd == ("use pikachu/post/wordpress/wordpress_user_enum") :
     os.system("clear")
     os.system("bash ~/../usr/share/Pikachu/modules/post/wordpress/wordpress_user_enum/wp_user.sh")
     Start()

######################################################
 else :
  print (Fore.RED + "[*] error")
  Start()









Start()


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
         os.system("rm -rf ~/../usr/share/Raticate")
         os.system("git clone https://github.com/Bananaj00e/Raticate.git ~/../usr/share/Raticate")
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
print (Fore.MAGENTA + "[*] Starting Raticate /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate |")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Pikachu |")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate |")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate /")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate |")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate -")
time.sleep(0.5)
os.system("clear")
print (Fore.MAGENTA + "[*] Starting Raticate /")
time.sleep(0.5)
time.sleep(2)
os.system("clear")
print(Fore.MAGENTA + "[*] Welcome To Raticate")
time.sleep(2.5)
os.system("clear")
##################################################" Pikatcu ############################################################

############### Random Logo ################

foo = ['2','3']
random = random.choice(foo)





if random == ("2") :
 print (Fore.MAGENTA + """


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
 print (Fore.MAGENTA + """

  //
 (")
 UU\    Little White Rabbit
 <><>*

---------------------------------------------

 """)


##########################Pikachu##########################


def Start() :

 commandd = input (Fore.MAGENTA + "[Raticate] >")


 if commandd == ("clear") :
  os.system("clear")
  Start()

 elif commandd == ("exit") :
  print (Fore.GREEN + "[*] Bye Bye :( ")

 elif commandd == ("help") :
  print(Fore.LIGHTYELLOW_EX + """
+
  ________________+ +
 |   Help Menu    |
 |----------------|____
+| show  | Show Modules|  +
 | use   | use Modules |
 | clear | Clear Screen|  +      +
 | exit  |  for exit   |
 | update|  For Update |
  ---------------------
+     +       +        +   +
+ +             +    +
  """)
  Start()

 elif commandd == ("update") :
  update = ("1.0")
  url = ("http://wiressouls.c1.biz/update.txt")
  ############################################  Update ######################################>
  web = urllib.request.urlopen(url)
  x = (web.read().decode())
  print (Fore.LIGHTYELLOW_EX + "The current version : ",update)
  print (Fore.LIGHTYELLOW_EX + "The current version : ",x)
  if update < x :
   os.system("clear")
   print (Fore.GREEN + "    Linux        Termux")
   print (Fore.GREEN + "     (1)          (2) ")
   ver = input (" >  ")
   if ver == "1" :
         updatelinux()
   elif ver == "2" :
         updatetermux()
  Start()
 
#########################Modules#####################


 elif commandd == ("show") :


  print (Fore.LIGHTYELLOW_EX + """

          Exploits                                    Rank                   Descrption
 ---------------------------






           Scanner
 ---------------------------






             Post
 ----------------------------
     raticate/post/openssh/ssh_user_enum                Normal         in Openssh 7.2 you can enumerate users
     raticate/post/wordpress/wordpress_user_enum        Good           in wordpress you can enumetate users




             Hash
 ----------------------------








   """)
  Start()

 elif commandd == ("use raticate/post/openssh/ssh_user_enum") :
    os.system("clear") 
    print("""


                            Username Enumration Openssh
                                                         1.0



     """)
    os.system("bash ~/../usr/share/Raticate/modules/post/openssh/ssh_user_enum/ssh_enum.sh")
    Start()
 elif commandd == ("use raticate/post/wordpress/wordpress_user_enum") :
     os.system("clear")
     print("""


                            Username Enumration WordPress
                                                         1.0



     """)

     os.system("bash ~/../usr/share/Raticate/modules/post/wordpress/wordpress_user_enum/wp_user.sh")
     Start()

######################################################
 else :
  print (Fore.RED + "[*] error")
  Start()









Start()


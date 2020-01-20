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

import subprocess
import  os
import sys
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
    time.sleep(0.01)

    bar.next()
bar.finish()
time.sleep(2)
os.system("clear")
print (Fore.GREEN + "[*] Current Version : ",update)
time.sleep(2)
print (Fore.GREEN + "[*] Last Version : ",x)
time.sleep(1.5)
os.system("clear")

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
  sys.exit()

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
     raticate/scanner/openssh/ssh_user_enum                Normal         in Openssh 7.2 you can enumerate users
     raticate/scanner/wordpress/wordpress_user_enum        Good           in wordpress you can enumetate users





             Post
 ----------------------------
     raticate/post/hydra/ssh_bruteforce                   Good
     raticate/post/hydra/ftp_bruteforce                   Good




             Hash
 ----------------------------
     raticate/hash/decrypt/base64                      Normal          fast base64 decrypter
     raticate/hash/decrypt/base32                      Normal          fast base32 decrypter
     raticate/hash/john/md5                            Good            decrypt md5 with john
     raticate/hash/john/sha1                           Good            decrypt SHA1 with john





   """)
  Start()

 elif commandd == ("use raticate/post/hydra/ssh_bruteforce") :
    os.system("clear")
    rc = subprocess.call(['which', 'hydra'])
    if rc == 0:
      os.system("clear")
      print (Fore.GREEN + "[*] Hydra Has Been Found")
      time.sleep(3)
    else:
       print (Fore.RED + "[*] [*] This Module Need Hydra , Please Install Hydra")
       Start()
    os.system("clear")
    time.sleep(4)
    os.system("clear")
    print (Fore.GREEN + "")
    os.system("bash ~/../usr/share/Raticate/modules/post/hydra/ssh_bruteforce/ssh.sh")
    Start()
 elif commandd == ("use raticate/post/hydra/ftp_bruteforce") :
    os.system("clear")
    rc = subprocess.call(['which', 'hydra'])
    if rc == 0:
      os.system("clear")
      print (Fore.GREEN + "[*] Hydra Has Been Found")
      time.sleep(3)
    else:
       print (Fore.RED + "[*] [*] This Module Need Hydra , Please Install Hydra")
       Start()
    os.system("clear")
    time.sleep(4)
    os.system("clear")
    print (Fore.GREEN + "")
    os.system("bash ~/../usr/share/Raticate/modules/post/hydra/ftp_bruteforce/ftp.sh")
    Start()

 elif commandd == ("use raticate/scanner/openssh/ssh_user_enum") :
    os.system("clear") 
    print(Fore.LIGHTYELLOW_EX + """


                            Username Enumration Openssh
                                                         1.0



     """)
    os.system("bash ~/../usr/share/Raticate/modules/scanner/openssh/ssh_user_enum/ssh_enum.sh")
    Start()
 elif commandd == ("use raticate/hash/decrypt/base64") :
     os.system("clear")
     print(Fore.LIGHTYELLOW_EX  + """


                                   Base64 Decrypter
                                                         by Bananaj00e



     """)

     os.system("bash ~/../usr/share/Raticate/modules/hash/decrypt/base64/base64.sh")
     Start()


 elif commandd == ("use raticate/hash/decrypt/base32") :
     os.system("clear")
     print(Fore.LIGHTYELLOW_EX  + """


                                   Base32 Decrypter
                                                         by Bananaj00e



     """)

     os.system("bash ~/../usr/share/Raticate/modules/hash/decrypt/base32/base32.sh")
     Start()




 elif commandd == ("use raticate/hash/john/md5") :
     os.system("clear")
     rc = subprocess.call(['which', 'john'])
     if rc == 0:
      os.system("clear")
      print (Fore.GREEN + "[*] John Has Been Found")
      time.sleep(3)
     else:
       print (Fore.RED + "[*] This Module Need John to Work, Please Install John")
       Start()
     os.system("clear")
     time.sleep(3)
     print (Fore.RED + "")
     os.system("bash ~/../usr/share/Raticate/modules/hash/john/md5/md5.sh")
     Start()

 elif commandd == ("use raticate/hash/john/sha1") :
     os.system("clear")
     rc = subprocess.call(['which', 'john'])
     if rc == 0:
      os.system("clear")
      print (Fore.GREEN + "[*] John Has Been Found")
      time.sleep(3)
     else:
       print (Fore.RED + "[*] This Module Need John to Work, Please Install John")
       Start()
     os.system("clear")
     time.sleep(3)
     print (Fore.RED + "")
     os.system("bash ~/../usr/share/Raticate/modules/hash/john/sha1/sha1.sh")
     Start()


 elif commandd == ("use raticate/scanner/wordpress/wordpress_user_enum") :
     os.system("clear")
     print(Fore.LIGHTYELLOW_EX  + """


                            Username Enumration WordPress
                                                         1.0



     """)

     os.system("bash ~/../usr/share/Raticate/modules/scanner/wordpress/wordpress_user_enum/wp_user.sh")
     Start()

######################################################
 else :
  print (Fore.RED + "[*] error")
  Start()









Start()


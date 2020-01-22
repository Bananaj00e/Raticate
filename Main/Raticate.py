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
         print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Updating")
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
bar =  Bar(Fore.WHITE +"[" +Fore.LIGHTYELLOW_EX  +"*" +  Fore.WHITE +"]" + Fore.WHITE + ' Checking For Updates', max=100)
for i in range(100):
    time.sleep(0.01)

    bar.next()
bar.finish()
time.sleep(2)
os.system("clear")
print (Fore.WHITE +"[" +Fore.GREEN +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Current Version : ",update)
time.sleep(2)
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Last Version : ",x)
time.sleep(1.5)
os.system("clear")

if x > update:
    time.sleep(4)
    print (Fore.WHITE +"[" +Fore.GREEN +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Update Found")
    time.sleep(4)

    os.system("clear")

    print(Fore.WHITE + """


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
    print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " No Update Found")
    time.sleep(4)
    os.system("clear")



################################################### Running #######################################################

time.sleep(3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate /")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate -")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate |")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate -")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate /")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate |")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate -")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate /")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate |")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate -")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate /")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate |")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate -")
time.sleep(0.3)
os.system("clear")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Starting Raticate /")
time.sleep(0.3)
os.system("clear")
##################################################" Pikatcu ############################################################

############### Random Logo ################

foo = ['2','1','3']
random = random.choice(foo)





if random == ("2") :
 print (Fore.WHITE + """


         __
        .. ~~-_     <==== You
   ___m<___m___~.___
   _|__|__|__|__|___|
   |__|__|__|__|__|_
    |_ |__|__|_|__|_|     <===== FireWall
   |__|__|__|_|__|__|
   ()))()()()())()())


  """)

elif random == ("1") :
 print (Fore.WHITE + """


 _______________
< Welcome To RcT! >
 ---------------
        \   ^__^
         \  (oo)-_______
            (__)|       )|/|
                ||----w |
                ||     ||



 """)
elif random == ("3") :
 print (Fore.WHITE + """

  //
 (")
 UU\    Little White Rabbit
 <><>*

---------------------------------------------

 """)


##########################Pikachu##########################


def Start() :

 commandd = input (Fore.WHITE + "[" + Fore.RED + "Raticate" + Fore.WHITE + "] >")


 if commandd == ("clear") :
  os.system("clear")
  Start()

 elif commandd == ("exit") :
  print (Fore.GREEN + "[*] Bye Bye :( ")
  sys.exit()

 elif commandd == ("help") :
  print(Fore.WHITE + """
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


  print (Fore.WHITE + """

          Exploits                                    Rank                   Descrption
 ---------------------------






           Scanner
 ---------------------------
     raticate/scanner/openssh/ssh_user_enum                Normal         in Openssh 7.2 you can enumerate users
     raticate/scanner/wordpress/wordpress_user_enum        Good           in wordpress you can enumetate users





             Post
 ----------------------------
     raticate/post/hydra/ssh_bruteforce                   Good        Brute Force SSH With Hydra
     raticate/post/hydra/ftp_bruteforce                   Good        Brute Force FTP With Hydra




             Hash
 ----------------------------
     raticate/hash/decrypt/base64                      Normal          fast base64 decrypter
     raticate/hash/decrypt/base32                      Normal          fast base32 decrypter
     raticate/hash/john/md5                            Good            decrypt md5 with john
     raticate/hash/john/sha1                           Good            decrypt SHA1 with john



            Payloads
-----------------------------
     raticate/listener/netcat_listner                 Good              Start Netcat listener
     raticate/payload/python/reverse_tcp              excelent         hashed python reverse shell 







   """)
  Start()


 elif commandd == ("use raticate/listener/netcat_listner") :
    rc = subprocess.call(['which', 'nc && xterm'])
    if rc == 1:
      os.system("clear")
      print (Fore.GREEN + "[*] netcat Has Been Found")
      time.sleep(1.6)
      print (Fore.GREEN + "[*] XTERM Has Been Found")
      time.sleep(3)
      os.system("clear")
      os.system("python3 ~/../usr/share/Raticate/modules/payloads/netcat/nc.py")
      Start()
    else:
       print (Fore.RED + "[*] This Module Need netcat and Xterm , Please Install it")
       print (Fore.RED + "[*] You Can Use Classic Netcat If You Dont Have Xterm : raticate/listener/classic_netcat_listener")
       Start()

 elif commandd == ("use raticate/listener/classic_netcat_listener") :
    rc = subprocess.call(['which', 'nc'])
    if rc == 0:
      os.system("clear")
      print (Fore.GREEN + "[*] Netcat Has Been Found")
      time.sleep(3)
      os.system("clear")
      os.system("python3 ~/../usr/share/Raticate/modules/payloads/netcat/classic_nc.py")
    else:
       print (Fore.RED + "[*] This Module Need Netcat , Please Install Netcat")
       Start()



 elif commandd == ("use raticate/payload/python/reverse_tcp") :
   os.system("clear")
   os.system("python3 ~/../usr/share/Raticate/modules/payloads/python/gen.py")
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


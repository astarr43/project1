import os
a=os.name
if a == "nt":
 print(a)
 os.system("ipconfig")
elif a == "posinx":
 print(a)
 os.system("ifconfig")
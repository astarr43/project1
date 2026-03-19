import hashlib
a = open("C:/Users/DELL/Downloads/VSCodeUserSetup-x64-1.108.1.exe",'rb')
data = a.read()
hash = hashlib.sha256(data).hexdigest()
a.close()
print(hash)
import subprocess

result = subprocess.run(
    ["dir"],
    capture_output=True,
    text=True,
    shell=True
).stdout

a=open("out.txt",'w')
a.writelines(result)
a.close()
a=open('out.txt','r')
print(a.read())
a.close()
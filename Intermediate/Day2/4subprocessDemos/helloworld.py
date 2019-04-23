import subprocess

pl = subprocess.Popen(["cmd", "/c","echo Hello Python"], stdout=subprocess.PIPE).communicate()[0]

print(pl)
print(pl.decode('utf-8'))
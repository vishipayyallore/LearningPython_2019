import subprocess


subprocess.Popen
pl = subprocess.Popen(["cmd", "/c", "dir"], stdout=subprocess.PIPE).communicate()[0]
print(pl.decode('utf-8'))
import subprocess


subprocess.Popen
pl = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE).communicate()[0]
print(pl.decode('utf-8'))
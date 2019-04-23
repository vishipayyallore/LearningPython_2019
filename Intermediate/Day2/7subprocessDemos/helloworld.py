import subprocess

pl = subprocess.Popen(["echo", "Hello Python"], stdout=subprocess.PIPE)

print(pl.communicate()[0])
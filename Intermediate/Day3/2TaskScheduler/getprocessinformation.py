import subprocess
import datetime

# Retrieving the processes information
subprocess.Popen
pl = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE).communicate()[0]

today = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
outputfilepath = f"./datastore/process_{today}.log"

with open(outputfilepath, 'a') as outputfile:
    outputfile.write(pl.decode('utf-8'))


"""This File is used for practice the programs daily
"""

import datetime

today = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
outputfilepath = f"./datastore/process_{today}.log"

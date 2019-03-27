#!/usr/bin/python
import requests
import json
import threading
import datetime
import time

currentDT = datetime.datetime.now()

def printGym():
    threading.Timer(900, printGym).start()
    r = requests.get("https://dasc.cyc.org.tw/api")
    fields = json.loads(r.text)

    gym_on = fields["gym"][0]
    swim_on = fields["swim"][0]

    print(gym_on, swim_on,str(currentDT))

printGym()
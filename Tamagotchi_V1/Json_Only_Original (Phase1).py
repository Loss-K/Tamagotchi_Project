# Back in the saddle again
# May 19th of 2022
# Last Updated

import threading
import time
import sys
import json
import os
import sqlite3
from datetime import date
from datetime import datetime

from pip._vendor.distlib.compat import raw_input

print("Initializing.. Checking if it's a first time setup.")
# For now, only check if the DB doesn't yet Exists - I want this because in the endgame,
# I'll be using this to determine when to introduce a quick tutorial
# how to play the game while the first time set up in the background begins.

dbtest = "test.db"

nodbexist = True

if not os.path.isfile(dbtest):
    nodbexist = True


if nodbexist:
    test = date.today()

    now = datetime.now()
    now2 = now.time()
    print(now)
    test2 = now2.isoformat(timespec='seconds')
    #test1 = test2.isoformat(timespec='seconds')

    nowint = (now.year*10000000000 +
      now.month * 100000000 +
      now.day * 1000000 +
      now.hour*10000 +
      now.minute*100 +
      now.second)

    db = sqlite3.connect("test.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS temp "
                "('id' INTEGER PRIMARY KEY,"
                "'date' date,"
                "'time' int,"
                "'stat_name' text,"
                "'stat_before' integer,"
                "'stat_after' integer,"
                "'self_pres' boolean)")


    #name = input("What do you want to name your Tamagotchi_V1?")
    #tz = input("What timezone are you in?")
    #print("Hi " + name + "!")

    #Any other set up

    #Add starting statistics
    self_pres_status = "False"

    cur.execute("INSERT INTO temp(date,time,stat_name,stat_before,stat_after,self_pres) "
                 "VALUES ('" + str(date.today()) + "'," + str(nowint) +
                 ",'BeginningPlay','100','100'," + "False" + ")")

    db.commit()

with open("Param.json", "r") as file:
    stat = json.load(file)

referencetohave = str(stat)
originalvalues = list(stat)

print("Data Started with")
print(referencetohave)


def background():
    # time_start = time.time()
    seconds = 0
    minutes = 0
    startfeeling = False

    print("Enter a Command: ")

    while True:
        # time.sleep(3)
        # sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
        # sys.stdout.flush()
        time.sleep(1)
        seconds += 1

        if seconds == 5:
            minutes += 1
            seconds = 0
            startfeeling = False

        if minutes % 5 == 0 and minutes > 1 and not startfeeling:
            hchange = 12.5
            schange = 16
            hychange = 6
            matho = False
            changevalues(hchange, schange, hychange, matho)
            startfeeling = True


def changevalues(hungerchange, sleepchange, hydratechange, math):

    for statname, aye in enumerate(originalvalues):

        temp = list(originalvalues[statname])

        if str(temp[0]) == "Hunger" and hungerchange > 0:
            if not math:
                prior= temp[1]
                temp[1] = temp[1] - hungerchange
                print("Hunger has decreased by " + str(hungerchange))
            if math:
                prior = temp[1]
                temp[1] = temp[1] + hungerchange
                print("Hunger has increased by " + str(hungerchange))
                if temp[1] > 100:
                    temp[1] = 100



            originalvalues[0][1] = temp[1]
          #  self_pres_status = "False"

            # cur.execute("INSERT INTO temp(date,time,stat_name,stat_before,stat_after,self_pres) "
            #             "VALUES ('" + str(date.today()) + "'," + str(nowint) +
            #             ",'" + str("Hunger") + "','" + str(prior) + "','" + str(temp[1]) + "'," + "False" + ")")
            #
            # db.commit()

        if str(temp[0]) == "Sleep" and sleepchange > 0:
            if not math:
                temp[1] = temp[1] - sleepchange
                print("Sleep has decreased by " + str(sleepchange))
            if math:
                temp[1] = temp[1] + sleepchange
                print("Sleep has increased by " + str(sleepchange))
                if temp[1] > 100:
                    temp[1] = 100
            originalvalues[1][1] = temp[1]

        if str(temp[0]) == "Hydration" and hydratechange > 0:
            if not math:
                temp[1] = temp[1] - hydratechange
                print("Hydration has decreased by " + str(hydratechange))
            if math:
                temp[1] = temp[1] + hydratechange
                print("Hydration has increased by " + str(hydratechange))
                if temp[1] > 100:
                    temp[1] = 100
            originalvalues[2][1] = temp[1]

    preservation()


def preservation():
    for statname, aye in enumerate(originalvalues):
        temp = list(originalvalues[statname])
        # if the stat is less than 20, the system is in danger of dying. It will attempt to save itself.
        if 20 >= temp[1] > 0:
            temp[1] = temp[1] + 10
            originalvalues[statname] = temp
            print(str(temp[0]) + " was neglected, I saved myself by having something that "
                                 "increased it by 10, current stat is " + str(temp[1]))
        elif temp[1] <= 0:
            print("I be ded. " + str(temp[0]) + " had a calculation of " + str(temp[1]))


def quitting():
    print("quitting")
    print("Saving the stats below")
    print(list(stat))
    with open("Param.json", "w") as json_file:
        json.dump(list(stat), json_file)

# now threading1 runs regardless of user input (Taken from
# https://stackoverflow.com/questions/31768865/
# how-to-use-threading-to-get-user-input-realtime-while-main-still-running-in-pyth
# until I understand more on threading. This code is modified from solution.


threading1 = threading.Thread(target=background)
threading1.daemon = True
threading1.start()

while True:
    command = raw_input().lower()
    hchange = 0
    schange = 0
    hychange = 0
    matho = True

    match command:
        case 'q':
            quitting()
            sys.exit()

        case 'f':
            hchange = 15
            changevalues(hchange, schange, hychange, matho)

        case 's':
            schange = 12
            changevalues(hchange, schange, hychange, matho)

        case 'w':
            hychange = 6
            changevalues(hchange, schange, hychange, matho)

        case unknown_command:
            print(f"Unknown command {unknown_command}")
# Back in the saddle again
# May 19th of 2022
# Last Updated

####
#### This is being rewritten using SQL to start databasing.
# At this time, It Does not pull in the data from the latest record if by chance the setup has been established.
# This is to prep for some modeling/ML.
# For now, I have it checking if the table exists, if not - create it. Using it as my marker.
# End product would have a table already in the back end - and it would just look for the beginning play row - to shave
# off time.

import threading
import time
import sys
import os
import sqlite3
from datetime import datetime
from pip._vendor.distlib.compat import raw_input


###### Any variable set ups
dbtest = "Tama_Stats.db"
Hunger = 10
Sleep = 0
Hydration = 0


def update_table(stat_name, prior_value, after, degrading_value, pres_status):
    db = sqlite3.connect("Tama_Stats.db")
    cur = db.cursor()
    now2 = (datetime.now().year * 10000000000 +
            datetime.now().month * 100000000 +
            datetime.now().day * 1000000 +
            datetime.now().hour * 10000 +
            datetime.now().minute * 100 +
            datetime.now().second)

    cur.execute("INSERT INTO stat_detail(datetime,stat_name,stat_before,stat_after,degrading,self_pres) "
                "VALUES ('" + str(now2) + "','" + str(stat_name) + "','" + str(prior_value) + "','" + str(after) +
                "','" + str(degrading_value) + "'," + str(pres_status) + ")")

    db.commit()
  #  cur.close()
  #  db.close()

#############################################################################################
def __init__():
    print("Initializing.. Checking if it's a first time setup.")
    # For now, only check if the DB doesn't yet exist - I want this because in the endgame,
    # I'll be using this to determine when to introduce a quick tutorial
    # how to play the game while the first time set up in the background begins.

    if not os.path.isfile(dbtest):
        db = sqlite3.connect(dbtest)
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS stat_detail "
                    "('id' INTEGER PRIMARY KEY,"
                    "'datetime' int,"
                    "'stat_name' text,"
                    "'stat_before' integer,"
                    "'stat_after' integer,"
                    "'degrading' boolean,"
                    "'self_pres' boolean)")

        update_table("BeginningPlay", "100", "100", "False", "False")

        #start variables
        Hunger = 100
        Sleep = 100
        Hydration = 100

        # name = input("What do you want to name your Tamagotchi_V1?")
        # tz = input("What timezone are you in?")
        # print("Hi " + name + "!")

        # Any other set up

        # Add starting statistics

        db.commit()
        cur.close()
        db.close()
    else:
        Sleep = resumevalues("Sleep")
        Hunger = resumevalues("Hunger")
        Hydration = resumevalues("Hydration")

#############################################################################################
######  Pull the latest Data
def resumevalues(valuetest):
    db = sqlite3.connect(dbtest)
    cur = db.cursor()
    curvalue = 0

    get_latest_stat = "SELECT stat_after FROM stat_detail WHERE stat_name =? ORDER BY ID DESC LIMIT 1 "
    cur.execute(get_latest_stat,(valuetest,))

    for row in cur:
        curvalue = row[0]

    cur.close()
    db.close()

    return curvalue
#############################################################################################

def background():
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

#############################################################################################
def doingmath(valuename,value, valuechange, optype):
    match optype:
        case True:
            result = value + valuechange
            if result > 100:
                result = 100
            print(f"{valuename} went from {value} to {result}")
            return result
        case False:
            result = value - valuechange
            print(f"{valuename} went from {value} to {result}")
            return result
def changevalues(hungerchange, sleepchange, hydratechange, math):

#############################Hunger#########################
        if hungerchange > 0:
            prior_value = Hunger
            updated_value = doingmath("Hunger", prior_value, hungerchange, math)
            match math:
                case True:
                    degrade = False
                    update_table("Hunger", str(prior_value), str(updated_value), str(degrade), "False")
                    print("True Case Hunger Completed.")
                case False:
                    degrade = True
                    update_table("Hunger", str(prior_value), str(updated_value), str(degrade), "False")
                    print("False Case Hunger Completed.")


#############################Sleep#########################
        if sleepchange > 0:
            prior_value = Sleep
            updated_value = doingmath("Sleep", prior_value, hungerchange, math)
            match math:
                case True:
                    degrade = False
                    update_table("Sleep", str(prior_value), str(updated_value), str(degrade), "False")
                    print("True Case Sleep Completed.")
                case False:
                    degrade = True
                    update_table("Sleep", str(prior_value), str(updated_value), str(degrade), "False")
                    print("False Case Sleep Completed.")
#############################Hydration#########################
        if hydratechange > 0:
            prior_value = Hydration
            updated_value = doingmath("Hydration", prior_value, hungerchange, math)
            match math:
                case True:
                    degrade = False
                    update_table("Hydration", str(prior_value), str(updated_value), str(degrade), "False")
                    print("True Case Hydration Completed.")
                case False:
                    degrade = True
                    update_table("Hydration", str(prior_value), str(updated_value), str(degrade), "False")
                    print("False Case Hydration Completed.")

#############################Self Preservation Check#########################
        # if temp[1] < 20 and not math:
        #     sp_needed = True
        # else:
        #     sp_needed = False
#############################Update Table#########################
        # if prior != temp[1] and math:
        #     update_table(str(temp[0]), str(prior), str(temp[1]), "False", "False")
        #     print("ok- table updated")
#############################Self Preservation Action#########################
        # if sp_needed:
        #     print("running Preservation plan")
        #     preservation()
        #     sp_needed = False

#############################Self Preservation Action#########################
# def preservation():
#     for statname, aye in enumerate(originalvalues):
#         temp = list(originalvalues[statname])
#         prior = temp[1]
#         # if the stat is less than 20, the system is in danger of dying. It will attempt to save itself.
#         if 20 >= temp[1] > 0:
#             temp[1] = temp[1] + 5
#             originalvalues[statname] = temp
#             print(str(temp[0]) + " was neglected, I saved myself by having something that "
#                                  "increased it by 5, current stat is " + str(temp[1]))
#             update_table(str(temp[0]), str(prior), str(temp[1]), "False", "True")
#         elif temp[1] <= 0:
#             print("I be ded. " + str(temp[0]) + " had a calculation of " + str(temp[1]))
#             update_table(str(temp[0]), str(prior), str(temp[1]), "True,", "True")
#             died()

#############################If you died - We don't really need?#########################
#It doesn't quit.
def died():
    print("You Died")
    quitting()

#############################Quitting used to save the json#########################
#Change it to check the tables/DB is closed?
def quitting():
    print("quitting")
    print("Saving the stats below")
    exit()


#############################Threading... Will be removed once buttons are there?#########################
# now threading1 runs regardless of user input (Taken from
# https://stackoverflow.com/questions/31768865/
# how-to-use-threading-to-get-user-input-realtime-while-main-still-running-in-pyth
# until I understand more on threading. This code is modified from solution.

# Definitely not the right order, nor the normal usage, but this will suffice for now.


__init__()


threading1 = threading.Thread(target=background)
threading1.daemon = True
threading1.start()
#############################Actions#########################
#Note: If Quitting runs via a non-command and a statement, there is a known error because it doesn't actually quit.
# I mean we need time to proceed
# Buttons and actions do interrupt time for about 1 second.
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

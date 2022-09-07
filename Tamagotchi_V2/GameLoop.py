import time
import sys

class theGameloop:
    def __init__(self, sdds_elapsed):
        self.seconds_elapsed = sdds_elapsed
        print(self.seconds_elapsed)
        #self.gameState = gameState

    def start_game(self):
        seconds = 0
        minutes = 0
        startfeeling = False

        while True:
            time.sleep(1)
            seconds += 1
            print(seconds)

            if seconds == 5:
                minutes += 1
                seconds = 0
                startfeeling = False

            if minutes % 5 == 0 and minutes > 1 and not startfeeling:
                hchange = -12.5
                schange = -16
                hychange = -6
                matho = False
                #changevalues(hchange, schange, hychange, matho)
                startfeeling = True
                print("Stats would decrease")
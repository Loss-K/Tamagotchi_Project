import time


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
        print(seconds)

        if seconds == 5:
            minutes += 1
            seconds = 0
            startfeeling = False

        if minutes % 5 == 0 and minutes > 1 and not startfeeling:
            hchange = 12.5
            schange = 16
            hychange = 6
            matho = False
            #changevalues(hchange, schange, hychange, matho)
            startfeeling = True

background()
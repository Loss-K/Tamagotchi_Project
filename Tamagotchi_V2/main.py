import Stats
import Tama
import UI_V4
import Background_Threads

#Later to have a prompt to create Tamagotchi and set the stats, fo now - ease of use is to set the good stuff.

stats = Stats.TStats(100, 100, 50)
bob = Tama.Tamagotchi("Bob", 0, stats)


#Bring up the UI and Tamagotchi
if __name__ == "__main__":
    Background_Threads.scheduler_job().plan_job()
    UI_V4.main()

import db_management

class TStats:
    def __init__(self, hunger, sleep, hydrate):
        self.hunger = hunger
        self.sleep = sleep
        self.hydrate = hydrate

    def hunger_change(self, amount_change):
        prior_hunger = self.hunger
        self.hunger += amount_change
        if self.hunger > 100:
            self.hunger = 100
        print(f"hunger went from {prior_hunger} to {self.hunger}")

    def sleep_change(self, amount_change):
        prior_sleep = self.sleep
        self.sleep += amount_change
        if self.sleep > 100:
            self.sleep = 100
        print(f"sleep went from {prior_sleep} to {self.sleep}")

    def hydrate_change(self, amount_change):
        prior_hydrate = self.hydrate
        self.hydrate += amount_change
        if self.hydrate > 100:
            self.hydrate = 100
        print(f"hydrate went from {prior_hydrate} to {self.hydrate}")

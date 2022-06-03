# This is in progress as I continue the training at 
# https://www.linkedin.com/learning/python-gui-development-with-tkinter-2

# Last Updated on June 3rd 2022

# To do:
# Graphics
# Customize Buttons
# Connect Functions

## Continue learning TKinter for more updates. (Currently a couple of modules in.
## Expect code to change once I complete the trainings and implement knowlegde.

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('350x350+50+200')
root.resizable(False,False)
root.title("Tamagotchi_V3")

happy = str(':)')
sad = str(':(')

tama = ttk.Frame(root)
tama.pack()
tama.config(padding=(100,100))
tamacharacter = ttk.Label(tama, text=happy).grid()

tama_two = ttk.Frame(root)

feedbutton = ttk.Button(tama_two, text= "feed Button",).grid(row=0,column=0)
drinkbutton = ttk.Button(tama_two, text= "drink Button").grid(row=0,column=1)
sleepbutton = ttk.Button(tama_two, text= "sleep Button").grid(row=0,column=2)
Saveandquit = ttk.Button(tama_two, text= "Save/Quit Button").grid(row=2,column=0, columnspan=3)
tama_two.pack()

# Temporary code so when testing can see a progress bar showing the runtime elapsing.
progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=250)
progressbar.config(value=50)
progressbar.pack()

feedbar = ttk.Progressbar(tama_two, orient=HORIZONTAL, length=50, value=25).grid(row=1,column=0)
drinkbar = ttk.Progressbar(tama_two, orient=HORIZONTAL, length=50, value=50).grid(row=1,column=1)
sleepbar = ttk.Progressbar(tama_two, orient=HORIZONTAL, length=50, value = 100).grid(row=1,column=2)


# This allows us to call the tkinter window
root.mainloop()

##################################
Introduction
##################################

When I learn any type of code, I try to think of a project that I can continuously work on as I continue to
work on my education. Sure, I plan to do more projects - but I like to have one consistent project helps me to improve
myself over time and improve my code.

While I have coded Python, I have had no structured training - This will change soon, but wanted to start putting
together what I know. As I learn, I will apply it. Not only on the lesson projects, but apply them on
one of my own. This is the first one.


##################################
Project Details
##################################

Tamagotchi is a popular game where one has to keep a little virtual creature alive. Failure to take care of this
virtual creature means it will suffer, and possibly virtually die. My project is the Tamagotchi project. However, I
plan to elevate this in some ways by adding some Machine Learning and potentially some AI functionality in the future.

###
I did a BEFORE learning Wireframe attempt below. Will be learning the proper way to build a wireframe along the way.
I will update this link when I do.
See the wireframe here: https://www.figma.com/file/B47LkEHldEXhJPxGlfDnF5/Tamagotchi-Project?node-id=0%3A1
###


##################################
To Do List and Notes
##################################

######    ######
Known Bug
######    ######
Commands currently provide Not found with my else statement - Since in the end I will have a GUI, this will be resolved later.

######    ######
 Reminder Notes
######    ######

TIME is not accurate. I have it set to decrease rapidly during testing runtimes

Revisit and cut down math lines

Record elapse time, so when the program is not running, it can do the appropriate math to show the expected change in
the stats.

Changed Values probably doesn't need safety statements. For testing they remain, at the end, can be removed. Especially
when the GUI will show the changes.

######    ######
Last Minute Ideas
######    ######

Modify code - Create First Time Run Function? (For starting values), Name Generation?

Send a ping when it needs attention (stats at 50% or less.)

Sleep takes time to recover - maybe replace with play until that can be coded in?

######    ######
   To Do List
######    ######

### Phase One ###

Create Stats to run off of
-How does the stat increase?
-How does the stat decrease?

Create some sort of way to save the stats in case the user has to go away
-Json File

Create a runtime timer

### Phase Two ###

Consider GUI
Simple Face :) :| :( to start
Action Buttons
-Eat
-Sleep
-Drink
Save/Quit

Status Bars for each state
Determine the math for the state on average (ie 47 Hunger, 29 Sleep, 9 Hydrate should be.. What?)

### Phase Three ###

Convert Json to a mini database
Considerations: How much data should retain?
Fields: Date/Time, Stat Name, Stat Change, Prior Value, Value After, Self Preservation

Record how often it's taken care of, versus Self Preservation.

### Phase Four ###
Animation to Graphics/GUI:
Tamagotchi animation 
Button Animation 
Flow between clicks 
Progress bar movement

### Phase Five ###
!!!! ML/AI -> I don't know too much about this yet, but the two ideas I have are listed below:

ML -> Machine Learning:
Use the DB to determine the occurrences and predict future actions and if the user met the future action,
or whether Self Preservation had to be taken.

AI -> Artificial Intelligence:
Instead of having the Self preservation code consistently checking per decrease
- use the ML data to determine ahead of time when to run the function itself.



#1)
from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)

rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

for trial in range(nTrials):
    rt_clock.reset()  # reset timing for every trial
    cd_timer.add(2) #add 2 seconds

    event.clearEvents(eventType='keyboard')  # reset keys for every trial
    count=-1 #reset the counter for every while loop
    while cd_timer.getTime() > 0: #for 2 seconds

        my_text.text = "Press a number as fast as you can %i" % trial
        my_text.draw()
        win.flip()

        keys = event.getKeys(keyList=['1', '2', 'escape'])  #collect keypresses after first flip

        if keys:
            count = count + 1
            if 'escape' in keys:
                win.close()
            if count = 0:
            resp_time = rt_clock.getTime() #use getTime to determine the response time
            print(keys, resp_time) #print keys and response times

win.close()

#2)Placement of ClearEvents is crutial because if you added it after line 25, this would give the cleared events no use 
#because of its placement after its collection.
#Script needs to count everytime a key get added so not indenting the final group of if loops affects this counting set up.

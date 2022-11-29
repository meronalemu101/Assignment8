from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os
import json as json

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1])

filename = 'subject1session1Nov212022'
main_dir = os.getcwd()
fullAddress = os.path.join(main_dir,'exp','data',filename)
if not os.path.exists(data_dir)
    os.makedirs(data_dir)
fullAddress = os.path.join(data_dir, filename)
print(fullAddress)

#blocks, trials, stims, and clocks
nBlocks= 2
nTrials= 4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
sub_resp = {0:[-1,-1,-1,-1], 1:[-2,-2,-2,-2]}
resp_time = {0:[-3,-3,-3,-3], 1:[-0,-0,-0,-0]}

sub_resp = [[-1]*nTrials]*nBlocks
sub_acc = [[-1]*nTrials]*nBlocks
prob = [[-1]*nTrials]*nBlocks
corr_resp = [[-1]*nTrials]*nBlocks
resp_time = [[-1]*nTrials]*nBlocks
blocks = [[0, 0, 0, 0], [1, 1, 1, 1]]
trails = [[0, 1, 2, 3], [0, 1, 2, 3]]

data_as_list = [prob, corr_resp, sub_resp, sub_acc, resp_time]
print(data_as_list) 



 #with open(block + fullAddress + mode='w') as sub_data:
        #data_writer = csv.writer(sub_data, delimiter=',')
        #for block in data: #loop over each block now
            #data_writer.writerow(block) #write a new row for that block
#with open(fullAdress, mode='w', newline '') as csvfile:
    #filednames = ['Block', 'Trial', 'SubjectResponse', 'ResponseTime']
    #writer = csv.DictWriter(csvfile, filednames=filednames)
    
    writer.writeheader()
    for iBlock in range(nBlocks):
        for iTrial in range(nTrials):
            writer.writerow({'Block': iBlock, 'Trial': iTrial,
            'SubjectResponse': responseData[iBlock]['SubjectResponse'][iTrial],
            'ResponseTime': responseData[iBlock]['ResponseTime'][iTrial]})
#create problems and solutions to show
#math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
#solutions = [4, 2, 1, 3] #write solutions
#prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count= -1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count + 1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 0 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial], 'reaction time', 
              resp_time[block][trial])
print(resp_time)
win.close()

with open(fullAddress, 'w') as sub_data:
    fieldnames = ['problem', 'corr_resp', 'sub_resp', 'sub_acc', 'resp_time']
    data_writer = csv.writer(sub_data, fieldnames = fieldnames)
    data_writer.writeheader()
        
    for block in range(nBlocks):
            for a,b,c,d in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
                data_as_dict.append({'block':a, 'trial':b,'problem':c,'corr_resp':d,'sub_resp':e,'sub_acc':f, 'resp_time': g})
            print(data_as_dict)
            for iTrail in range(nTrials):
            data_writer.writerow(data_as_dict(iTrial)

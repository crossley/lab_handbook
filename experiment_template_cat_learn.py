# import useful things
from psychopy import visual, event, core
import numpy as np

# initialise whatever
n_trials = 10

# for now just create random numbers for grating sf and ori
x = np.random.normal(50, 10, n_trials)
y = np.random.normal(50, 10, n_trials)
cat = np.concatenate(np.ones(n_trials//2), 2*np.ones(n_trials//2))

# what behaviour do you want to record?
x_record = []
y_record = []
ca_record = []
resp_record = []
rt_record = []

# create a grating
stim = visual.gratingStim()

# create two clocks
# one clock for the entire experiment
# one clock for the states
exp_clock = core.Clock() 
state_clock = core.Clock()

# What is the initial state?
state = "iti"

# jump into a while loop / state machine
current_trial = 0
while True:

    if state == "iti":
        stim.sf = x[current_trial]
        stim.ori = y[current_trial]

    if state_clock.getTime() > 1.0
        stim.draw()
        state = "stim"
        state_clock.reset()

    if state == "stim":
        pass

    if state == "feedback":
        pass

    if state == "record_trial":
        current_trial += 1
        pass
    
    # it's generally a good idea to have a universal exit
    # chunk
    # if exit:
    #   close all windows etc.

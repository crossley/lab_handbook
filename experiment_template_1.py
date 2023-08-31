# import useful things

# initialise whatever

# create two clocks
# one clock for the entire experiment
# one clock for the states
# clock_exp = ...
# clock_state = ...

# jump into a while loop / state machine

while True:

    if state == "state_1":
        # start the state timer
        # draw whatever you want to draw
        # specify state transition condition
        # E.g.
        if key_pressed:
            state_exit = True

        # E.g., 
        if state_clock.getTime() > 3.0
            state_exit = True

        if state_exit == True:
            # set whatever needs to be set before landing in
            # the next state / clean up etc.

            # reset state clock

            # transition to the next state
            # state = "state_2"
            pass
        pass

    if state == "state_2":
        pass

    if state == "state_3":
        pass
    
    # it's generally a good idea to have a universal exit
    # chunk
    # if exit:
    #   close all windows etc.

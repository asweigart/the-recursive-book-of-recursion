def theLoop(i):
    if i < 4: # Stops when false.
        # The main code:
        if i == 2: # The break condition.
            # BASE CASE
            return
        # RECURSIVE CASE
        print(i, 'Hello!')
        theLoop(i + 1) # Increment i.
        return
    else:
        # BASE CASE
        return

theLoop(0) # Start i at 0.
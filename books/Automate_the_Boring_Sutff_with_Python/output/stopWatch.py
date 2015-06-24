import time

# Display the program's instructions.
print('Press ENTER to begin. Afeterwards, press ENTER to "click" the stopwatch.')
print('Press Ctrl-C to quit.')
raw_input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.
try:
    while True:
        raw_input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #{}: {} ({})'.format(lapNum, totalTime, lapTime))
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
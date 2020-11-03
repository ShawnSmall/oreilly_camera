#! /usr/bin/env python3

# Spy-Pi code version 1
# this code takes an image every minute (60 seconds), 
# and overwrites the current image with the new one
import os
import time
# choose a delay time in seconds by modifying the next line
delay = 60
# below are the default location to put the files, and the name to use
directory = "/home/pi/oreilly_camera "
filename = "spycam"
stem = ".jpg"
webfile = directory + filename + stem
# and this is the command to run.
mycommand = "fswebcam -d /dev/video0 -r 640x480 --no-banner"
# this is the actual 'do stuff' part. It runs forever
while True:
    runme = mycommand + " " + webfile
    os.system(runme)
    time.sleep(delay)

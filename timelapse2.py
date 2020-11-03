# Spy-Pi code version 2
# takes an image every minute, and saves 1 week (7 days) of data
# it also makes the most current image available 
import os
import time
import shutil
# choose a delay time in seconds by modifying the next line
delay = 60
# this says to save 7 days (1 week) at a time, feel free to change to a different duration
savedays = 7
# do not change this math code, it converts our savedays to how often to retake a pic in secs
# note that 1 day at 1 picture/minute is 10,080 files per week
waitcount = savedays * 24 * 60 * 60 / delay
# below are the default location to put the files, and the name to use
directory = '/home/pi/web/'
filename = "spycam"
stem = ".jpg"
# also, this is the file the webserver expects
webfile = directory + filename + stem
# and this is the command to run.
mycommand = "fswebcam -d /dev/video0 -r 640x480 --no-banner"
# this is the actual 'do stuff' part. It runs forever
icount = 0
while True:
    icount += 1
    myfile = directory + filename + "_" + str(icount) + stem
    runme = mycommand + " " + myfile
    os.system(runme)
    # copy new file to the webfile location so it is web-visible
    shutil.copy(myfile, webfile)
    # new purge routine removes older images after expiration time
    inix = icount - waitcount
    if inix > 0:
        deleteme = directory + str(inix) + filename + stem
        os.remove(deleteme)
        time.sleep(delay)

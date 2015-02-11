################################################################################
# Imports ######################################################################
################################################################################

import time, commands, os
import RPi.GPIO as GPIO
import pygame

################################################################################
# Setup ########################################################################
################################################################################

GPIO.setmode (GPIO.BCM)

GPIO.setup(17, GPIO.IN) # Button 1
GPIO.setup(18, GPIO.IN) # Button 2
GPIO.setup(27, GPIO.IN) # Button 3
GPIO.setup(22, GPIO.IN) # Button 4
GPIO.setup(23, GPIO.IN) # Button 5
GPIO.setup(24, GPIO.IN) # Button 6
GPIO.setup(25, GPIO.IN) # Button 7

os.system('pkill omxplayer')
print "Playing Loop"
os.system('omxplayer -b -o local Desktop/videos/square/loop/loop.mov &')

button_1 = 0; button_2 = 0; button_3 = 0; button_4 = 0
button_5 = 0; button_6 = 0; button_7 = 0

################################################################################
# Main Video Control ###########################################################
################################################################################

# Background to hide code when videos change
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(0)

while True:
    if GPIO.input(17) and not button_1:
        os.system('pkill omxplayer'); button_1 = 1
        print "Playing Mike"
        os.system('omxplayer -b -o local Desktop/videos/square/Mike.mp4 &')

    if GPIO.input(18) and not button_2:
        os.system('pkill omxplayer'); button_2 = 1
        print "Playing Moen - Dodgeballs"
        os.system('omxplayer -b -o local Desktop/videos/square/moen_dodgeballs.mp4 &')

    if GPIO.input(27) and not button_3:
        os.system('pkill omxplayer'); button_3 = 1
        print "Playing Moen - Shoppingcart"
        os.system('omxplayer -b -o local Desktop/videos/square/moen_shoppingcart.mp4 &')

    if GPIO.input(22) and not button_4:
        os.system('pkill omxplayer'); button_4 = 1
        print "Playing Chips Ahoy! - Hidden Camera"
        os.system('omxplayer -b -o local Desktop/videos/square/chipsahoy_hiddencamera.mov &')

    if GPIO.input(23) and not button_5:
        os.system('pkill omxplayer'); button_5 = 1
        print "Playing Light of Human Kindness Reel"
        os.system('omxplayer -b -o local Desktop/videos/square/LOHK_short.mp4 &')

    if GPIO.input(24) and not button_6:
        os.system('pkill omxplayer'); button_6 = 1
        print "Playing RVA Makerfest"
        os.system('omxplayer -b -o local Desktop/videos/square/rva_makerfest.mp4 &')

    if GPIO.input(25) and not button_7:
        os.system('pkill omxplayer'); button_7 = 1
        print "Playing Partybot Reel"
        os.system('omxplayer -b -o local Desktop/videos/square/partybot_reel.mov &')

    if not GPIO.input(17): button_1 = 0
    if not GPIO.input(18): button_2 = 0
    if not GPIO.input(27): button_3 = 0
    if not GPIO.input(22): button_4 = 0
    if not GPIO.input(23): button_5 = 0
    if not GPIO.input(24): button_6 = 0
    if not GPIO.input(25): button_7 = 0

    if not 'omxplayer' in commands.getoutput('ps -A'):
        print "Playing Loop"
        os.system('omxplayer -b -o local Desktop/videos/square/loop/loop.mov &')

################################################################################
################################################################################
################################################################################

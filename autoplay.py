#On Chrome, when you try to access a 
# website and your internet is down, you see a 
# little dinosaur. (Apparently because dinosaurs 
# have short arms and they "can't reach" your website.
#On this page, there is a hidden game, 
# if you hit space bar you can play the T-rex run game.

#Alternatively you can access the game directly here:
#https://elgoog.im/t-rex/
#You goal today is to write a Python script to 
# automate the playing of this game. Your program will look at 
# the pixels on the screen to determine when it needs to hit the
# space bar and play the game automatically.
#You can see what it looks like when the game is automated with 
# a bot:
#https://elgoog.im/t-rex/?bot

#You might want to look up these two packages:
#https://pypi.org/project/Pillow/
#https://pyautogui.readthedocs.io/en/latest/

#High score 1338

import pyautogui
import keyboard
import time
import math

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# print(screenWidth, screenHeight)


# the intervals where the bot will search for obstacles
x_start, x_end = 500, 533

last = 0
total_time = 0

width = 1360


# Scaled down coordinates for a 1360x768 display
scaled_coordinates = (int(530), int(425)), (int(671), int(388))
dino_ground = (417,415)   

time.sleep(1)         

keyboard.press(' ')        
# Main game loop
while True:
    t1 = time.time()
    # Check the current image on the screen
    image = pyautogui.screenshot()
    
    #This needs more finetuning
    if math.floor(total_time) != last:
        x_end += 1
        if x_end >= width:
            x_end = width
        last = math.floor(total_time)

    
    if image.getpixel(scaled_coordinates[1]) == (247, 247, 247):
        print("game over")
        break

# Check if there's an obstacle in front of the T-Rex
#This basically is true all the time   
#Lets check first with the mouse coords then fine the exact ones for my screen
#Also find the rgb value 
    #if image.getpixel(scaled_coordinates[0]) == (83, 83, 83) or image.getpixel((530, 410)) == (83,83,83):
        # If there's an obstacle, jump over it
        #pyautogui.press('space')
        #print(image.getpixel(scaled_coordinates[0]))
    for x in reversed(range(x_start ,x_end)):
        for y in range (410,425):
            if image.getpixel((x, y)) == (83,83,83):      
                #if image.getpixel(dino_ground) == (247,247,247 ):
                keyboard.press(' ') 
                break
            
    t2 = time.time()-t1
    total_time += t2
         
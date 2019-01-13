#!/usr/bin/env python3
"""
Vector channels Hal

code displays Hal.jpg file to screen and delivers Hal's famous one liner to Dave

Creative Commons Liscence  written by J. U'Ren	jim.uren@gmail.com  2019-01-05
"""

import anki_vector
import time
from PIL import Image

with anki_vector.Robot() as robot:
    image = Image.open('Hal.jpg')    # JPEG file to be displayed

    screen_data = anki_vector.screen.convert_image_to_screen_data(image)  
   
    #clears Vector's eyes from screen
    robot.screen.set_screen_to_color(anki_vector.color.off, duration_sec=0.0)
    robot.screen.set_screen_with_image_data(screen_data,5.0)
    
    #displays JPEG image to screen
    robot.screen.set_screen_with_image_data(screen_data,10.0)

    time.sleep(2.0)

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        # print("Say 'I am sorry Dave  I am afraid I can't do that'...")
        robot.say_text("I am sorry Dave - I am afraid I can't do that")



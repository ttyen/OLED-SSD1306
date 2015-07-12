from ssd1306.ssd1306 import ssd1306_driver
import time
import sys
#import os

#from AdaFruit example
# import Image
# import ImageDraw
# import ImageFont


led = ssd1306_driver()
led.begin()
led.clear_display()

offset = 0 # flips between 0 and 32 for double buffering



# Load default font. From AdaFruit example
#font = ImageFont.load_default()

from ssd1306.fonts import  arial_narrow_16, arial_16

## Font code from original sample
#font =  arial_narrow_16  # fonts are modules, does not need to be instantiated
    # draw_text3 returns the col position following the printed text.
#x = led.draw_text3(0,0,'Hello World',font)  

# text_width returns the width of the string in pixels, useful for centering:
# text_width = led.text_width('Hello World',font)
# x = (128-text_width)/2
# led.draw_text3(x,0,'Hello World',font)



while True:

    # write the current time to the display on every other cycle
    if offset == 0:

        # retrieve current date and time
        # text = time.strftime("%d %b %H:%M")
        # text = time.strftime("%T")
        # text = time.strftime("%b %d %Y %H:%M:%S", time.gmtime())
        text = time.strftime("%b %d %Y %H:%M:%S", time.localtime())
        led.draw_text2(0,0,text,1)

        text = "GROUND CONTROL:"
        # led.draw_text2(0,42,text,1)
        led.draw_text2(0,14,text,1)

        # led.draw_text3(0,0,'Ground Control:',font)

        text = "Commence countdown"
        # led.draw_text2(0,52,text,1)
        led.draw_text2(0,24,text,1)

#       led.draw_text3(0,0,'Hello World',font)
        # text = "Navigation: Running..."
        # led.draw_text2(0,24,text,1)

# SEE README FOR ADDITIONAL INFO ON CHARACTER/SYMBOL USAGE: https://github.com/HudsonWerks/ssd1306, esp. degrees
#        textSize = led.draw_text3(0,0,'451\177F', font)
	
	    #led.draw_image("/root/slatsmall.png",0,32);
        # led.draw_image("/root/mars_rover.png",0,32);
        # led.draw_text2(60,32,"Piranha",1)
        # led.draw_text2(60,45,"Status: OK",1);
        led.draw_text2(0,42,"ENGINES",1)
        led.draw_text2(0,52,"Status: ON",1);

    #	led.draw_image("/root/piranha.png",0,32);

#        led.draw_progress(10, 100, 20, 40, width=128, height=5);

        led.display()
        time.sleep(4)
    else:
        time.sleep(4)
  
    # vertically scroll to switch between buffers
    for i in range(0,32):
        offset = (offset + 1) % 64
        led.command(led.SET_START_LINE | offset)
        time.sleep(0.05)

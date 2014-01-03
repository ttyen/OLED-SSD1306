from ssd1306.ssd1306 import ssd1306_driver
import time
import sys

led = ssd1306_driver()
led.begin()
led.clear_display()

offset = 0 # flips between 0 and 32 for double buffering

while True:

    # write the current time to the display on every other cycle
    if offset == 0:
	text = "Reef #10"
        led.draw_text2(0,0,text,2)
        text = "Vehicle Status: OK"
        led.draw_text2(0,16,text,1)
        text = "Navigation: Running..."
        led.draw_text2(0,24,text,1)
	
	#led.draw_image("/root/slatsmall.png",0,32);
	#led.draw_text2(60,32,"Piranha",1)
	#led.draw_text2(60,45,"Status: OK",1)
	#led.draw_image("/root/piranha.png",0,32);

        led.display()
        time.sleep(2)
    else:
        time.sleep(2)
        
    # vertically scroll to switch between buffers
    for i in range(0,32):
        offset = (offset + 1) % 64
        led.command(led.SET_START_LINE | offset)
        time.sleep(0.01)

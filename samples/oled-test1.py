## Written by Charles A. Hamilton, HudsonWerks LLC

from ssd1306.ssd1306 import ssd1306_driver
from ssd1306.fonts import arial_narrow_16, arial_16
import time
import sys

led = ssd1306_driver()
led.begin()
led.clear_display()

offset = 0 # flips between 0 and 32 for double buffering

while True:

    # write the current time to the display on every other cycle
    if offset == 0:
        # retrieve current date and time
        text = time.strftime("%b %d %Y %H:%M:%S", time.localtime())
        led.draw_text2(0,0,text,1)

        text = "GROUND CONTROL:"
        led.draw_text2(0,14,text,1)
        text = "Commence countdown"
        led.draw_text2(0,24,text,1)

        led.draw_text2(0,42,"ENGINES",1)
        led.draw_text2(0,52,"Status: ON",1);

        led.display()
        time.sleep(4)
    else:
        time.sleep(4)
  
    # vertically scroll to switch between buffers
    for i in range(0,32):
        offset = (offset + 1) % 64
        led.command(led.SET_START_LINE | offset)
        time.sleep(0.05)

from ssd1306.fonts import arial_16
from ssd1306.ssd1306 import ssd1306_driver
led = ssd1306_driver()
led.begin()
led.clear_display()
font = arial_16  # fonts are modules, does not need to be instantiated
# draw_text3 returns the col position following the printed text.
x = led.draw_text3(0,0,'Hello World',font)  
led.display()
# text_width returns the width of the string in pixels, useful for centering:
text_width = led.text_width('Hello World',font)
x = (128-text_width)/2
led.draw_text3(x,20,'Hello World',font)
led.display()

from ssd1306.ssd1306 import ssd1306_driver
led = ssd1306_driver()
led.begin()
led.clear_display()
led.draw_text2(0,0,'Hello World',2)
led.display()
led.draw_text2(20,20,'Hello World',1)
led.display()

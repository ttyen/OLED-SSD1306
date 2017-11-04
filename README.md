ssd1306-bbb
===========

A library for interfacing the SSD1306 OLED display with the BeagleBone Black.
Based off of [py-gaugette](https://github.com/guyc/py-gaugette) by Guy Carpenter.
With modified sample code by Charles A. Hamilton

Wiring OLED -> BBB
===================
GND      -> P9-1

VCC      -> P9-3

D0(SCL)  -> P9-22

D1(SDA)  -> P9-18

RES      -> P9-12

DC       -> P9-15


Prerequisites
=============

### Adafruit BBIO

The [Adafruit BeagleBone Black IO library](https://aur.archlinux.org/packages/python2-bbio/) is required for GPIO manipulation (available in AUR).

SPI setting:
Beaglebone Black pin configuration:
RST = 'P9_12'
Note the following are only used with SPI:
DC = 'P9_15'
SPI_PORT = 1
SPI_DEVICE = 0

BBB: Debian 7.9, python 2.7.3

OLED: 6 pins, OLED Driver IC: SSD1306, Resolution: 128 x 64
http://www.rhydolabz.com/displays-c-88/096-oled-display-module-spii2c-128x64-6-pin-white-p-2260.html

Basic Usage
==================

```python
    from ssd1306.ssd1306 import ssd1306_driver
    led = ssd1306_driver()
    led.begin()
    led.clear_display()
    led.draw_text2(0,0,'Hello World',2)
    led.display()
```

Drawing Images
==================
The PIL library is used to draw images to the screen. Remember to pre-scale your image!

```python
    led = ssd1306_driver()
    led.begin()
    led.clear_display()
    led.draw_image("/home/debian/OIT.png",0,32)
    led.display()
```

Font Usage
==================

```python
    from ssd1306.fonts import arial_16
    font = arial_16  # fonts are modules, does not need to be instantiated
    # draw_text3 returns the col position following the printed text.
    x = led.draw_text3(0,0,'Hello World',font)  

    # text_width returns the width of the string in pixels, useful for centering:
    text_width = led.text_width('Hello World',font)
    x = (128-text_width)/2
    led.draw_text3(x,0,'Hello World',font)
```

The fonts include the printable ASCII characters ('!' through '~') and because of the usefulness of the degree symbol '&deg;', it has been added as a non-standard character 127 (0x7F hex and 177 octal).  Use the degree symbol in a python literal like this: 
```python
textSize = led.draw_text3(0,0,'451\177F', font)
```


Installation:
=============
git clone https://github.com/ttyen/OLED-SSD1306

cd OLED-SSD1306

python setup.py install


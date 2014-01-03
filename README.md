ssd1306-bbb
===========

A library for interfacing the SSD1306 OLED display with the BeagleBone Black.
Based off of [py-gaugette](https://github.com/guyc/py-gaugette) by Guy Carpenter.

Prerequisites
=============

### Adafruit BBIO

The [Adafruit BeagleBone Black IO library](https://aur.archlinux.org/packages/python2-bbio/) is required for GPIO manipulation (available in AUR).

### py-spidev

To communicate with the OLED display,  [spidev](https://github.com/doceme/py-spidev) is required (available in AUR).

### PIL 

To render image files to the OLED display [PIL](http://www.pythonware.com/products/pil/) is required (available in standard repositories).

SSD1306 OLED Usage
==================

```python
    import ssd1306.ssd1306
    RESET_PIN = 15 # optional, defaults to 15
    DC_PIN    = 16 # optional, defaults to 16
    led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
    led.begin()
    led.clear_display()
    led.draw_text2(0,0,'Hello World',2)
    led.display()
```

SSD1306 Font Usage
==================

```python
    from gaugette.fonts import arial_16
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



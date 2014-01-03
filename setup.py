#!/usr/bin/env python

from distutils.core import setup

setup(name='ssd1306',
      version='0.1',
      description='Python library for the SSD1306 OLED display with the BeagleBone Black',
      author='Ethan Zonca',
      author_email='e@ethanzonca.com',
      url='http://bitbucket.com/normaldotcom/python2-ssd1306-bb/',
      license = 'LICENSE.txt',
      packages = ['ssd1306', 'ssd1306.fonts']
)

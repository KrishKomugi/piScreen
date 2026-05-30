#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch4
from PIL import Image,ImageDraw, ImageFont

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)
try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    #disp = LCD_2inch4.LCD_2inch4(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_2inch4.LCD_2inch4()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()
    
    ##From midpoint, split image in half and swap sides
    im = Image.open("../pic/milkyWay.png")
    xsize, ysize = im.size
    sideL = im.crop((0,0,xsize//2,ysize//2))
    im.paste(0,0)

    #draw a cross onto the image
    draw = ImageDraw.Draw(im)
    draw.line((0,0) + im.size, fill = 128)
    draw.line((0, im.size[1], im.size[0], 0),fill=128)
    disp.ShowImage(im)
    im.show()

    Font1 = ImageFont.truetype("../Font/Font01.ttf",25)


    while True:
        pass

    disp.clear()
    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
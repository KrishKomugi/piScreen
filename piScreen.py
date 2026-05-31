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


# functions go here

#prompt user to select image
def imageSelect():
    files  = {}
    for i, image in enumerate(os.listdir("img/"), start =1):
         files[i]=image

    while True:
        for key in files:
            print(f"{key}. {files[key]}")
        try:
            return Image.open("img/"+files[int(input("Enter the number of the image you would like to select: "))])
        except IOError:
            print("\nInvalid selection")
            print(40*"*")



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
    
    # code goes here

    # open image
    im = imageSelect()




    # end of program cycle 
    disp.clear()
    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()

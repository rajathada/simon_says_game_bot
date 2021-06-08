# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 18:05:39 2021

@author: rajat
"""

import time
import pyautogui
from PIL import ImageGrab
from mss import mss
import numpy as np

scroll_n = -400
start_position = (900,500)
TL = (800,400) #TOP_LEFT
TR = (1100,400) #TOP_RIGHT
BL = (800,700) #BOTTOM_LEFT
BR = (1100,700) #BOOTOM_RIGHT

C_G_TL = (52,232,158) #Color with Glow Top Left - Green
C_G_TR = (239,59,54) #Color with Glow Top Right - Red
C_G_BL = (255,195,113) #Color with Glow Bottom Left - yellow
C_G_BR = (28,181,224) #Color with Glow Bottom Right - Blue

C_TL = (87,141,139) #Color without Glow Top Left - Green
C_TR = (143,89,108) #Color without Glow Top Right - Red
C_BL = (148,130,126) #Color without Glow Bottom Left - Yellow
C_BR = (80, 126, 159) #Color without Glow Bottom Right

im_cache = ImageGrab.grab()

def scroll(scroll_n):
    pyautogui.scroll(scroll_n)
    
def click(position):
    time.sleep(.1)
    pyautogui.click(x=position[0], y=position[1])

def image_analyses():
    n_color_seq = 1
    click_seq = []
    j = 0
    global im_cache
    while True:
        
        im = ImageGrab.grab()
        #im.save(f'{j}.png')
        if im.getpixel(TL)[1] > 225 and im != im_cache and im.getpixel((900,500))[2] == 68: #im.getpixel(TL) == C_G_TL :
            click_seq.append(TL)
            #im.save(f'{n_color_seq}_{j}.png')
            #print(click_seq)
            #print(n_color_seq)
            #while im == ImageGrab.grab():
            #   pass
        elif im.getpixel(TR)[0] > 230 and im.getpixel(TR)[1] < 65 and im != im_cache and im.getpixel((900,500))[2] == 68: #im.getpixel(TR) == C_G_TR and im != im_cache:
            click_seq.append(TR)
            #im.save(f'{n_color_seq}_{j}.png')
            #print(click_seq)
            #print(n_color_seq)
            #while im == ImageGrab.grab():
            #   pass
        elif im.getpixel(BL)[0] > 250 and im.getpixel(BL)[1] > 190 and im != im_cache and im.getpixel((900,500))[2] == 68: # im.getpixel(BL) == C_G_BL and im != im_cache:
            click_seq.append(BL)
            #im.save(f'{n_color_seq}_{j}.png')
            print(click_seq)
            print(n_color_seq)
            #while im == ImageGrab.grab():
            #   pass
        elif im.getpixel(BR)[2]>220 and im != im_cache and im.getpixel((900,500))[2] == 68: #im.getpixel(BR) == C_G_BR: and im != im_cache:
            click_seq.append(BR)
            #im.save(f'{n_color_seq}_{j}.png')
            #print(click_seq)
            #print(n_color_seq)
            #while im == ImageGrab.grab():
            #   pass
        print(click_seq)
        print(n_color_seq)
        if len(click_seq) == n_color_seq:
            time.sleep(1)
            for i in click_seq:
                click(i)
                
            click_seq.clear()
            n_color_seq += 1
         
        if n_color_seq > 15:
            break
        
        im_cache = im.copy()
        j += 1

if __name__ == '__main__':
    time.sleep(2)
    scroll(scroll_n)
    click(start_position)
    image_analyses()
    

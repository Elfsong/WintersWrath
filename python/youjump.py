#coding: utf-8

import os

def jump(factor, distance):
    press_time = int(distance * 1000 / factor)
    cmd = 'adb shell input swipe 1 1 2 2 ' + str(press_time)
    os.system(cmd)

if __name__ == "__main__":
    factor = float(raw_input("Please input jump factor: "))
    
    while True:
        distance = float(raw_input("Please input distance: "))
        jump(factor, distance)

    
    

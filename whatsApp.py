import pyautogui as pg
import time
time.sleep(10)
txt = open('animal.txt', 'r')
a = "You are a"

for i in txt:
    pg.write(a+' '+i)
    pg.press('Enter')
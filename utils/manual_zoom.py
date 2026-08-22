#import keyboard
import pyautogui as pag
from time import *
import pynput
tab=5


keyboard_=pynput.keyboard.Controller()
state=True
def zoom():
    global state, keyboard_
    print("state1")
    #pag.hotkey("esc")
    keyboard_.press(pynput.keyboard.Key.esc)
    sleep(0.01)
    for _ in range(tab):
        #pag.hotkey("tab")
        sleep(0.01)
        keyboard_.press(pynput.keyboard.Key.tab)
        sleep(0.01)
    #!
    #pag.hotkey("enter")
    keyboard_.press(pynput.keyboard.Key.enter)
    sleep(0.01)
    #for _ in range(180):
    #    keyboard_.press(pynput.keyboard.Key.left)
    #    sleep(0.01)
    if state:
        print("state1")
        pag.moveTo(670, 150)
    if not state:
        print("state2")
        pag.moveTo(1245, 150)
    pag.click()
    sleep(0.01)
    keyboard_.press(pynput.keyboard.Key.esc)
    sleep(0.01)
    keyboard_.press(pynput.keyboard.Key.esc)
    sleep(0.01)
    keyboard_.press(pynput.keyboard.Key.f12)
    state=not state


cmb=[{pynput.keyboard.Key.f2}]
current = set()
def on_press(key):
    if any([key in z for z in cmb]):
        current.add(key)
        if any(all(k in current for k in z) for z in cmb):
            zoom()
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()

#keyboard.add_hotkey('f2', test)
#keyboard.wait()
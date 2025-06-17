import pyautogui as auto
import time
from pynput import keyboard
import threading
import random

running = True

def on_press(key):
    global running
    try:
        if key == keyboard.Key.esc:
            print("ESC pressionado, saindo...")
            running = False
            # Para o listener
            return False
    except AttributeError:
        pass

# Inicia o listener em uma thread separada para não travar o loop principal
listener = keyboard.Listener(on_press=on_press)
listener.start()

centro_x = 708
centro_y = 481

delta_x = 150
delta_y = 130

while True:
    if not running:
        break
    for i in range(10):
        for i in range(5):
            auto.moveTo(centro_x, centro_y)
            match(i):
                case(0):
                    arrastar_x = centro_x + delta_x
                    arrastar_y = centro_y - delta_y
                case(1):
                    arrastar_x = centro_x
                case(2):
                    arrastar_x = centro_x - delta_x
                case(3):
                    arrastar_x = centro_x+delta_x
                    arrastar_y = centro_y
                case(4):
                    arrastar_x = centro_x-delta_x
            auto.mouseDown()
            auto.dragTo(arrastar_x, arrastar_y, duration=0.5)
            auto.mouseUp()
        auto.scroll(-(random.randint(3, 5)) + random.randint(0, 1))     
    auto.scroll(100)                       

print("Programa finalizado.")

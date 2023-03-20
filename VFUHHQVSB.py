import pyautogui
from datetime import datetime
from time import sleep


while True:
    now = datetime.now()
    dt_str = now.strftime("%d-%m-%Y-%H-%M-%S")

    shot = pyautogui.screenshot()
    shot.save(f'VFUHHQVKRWV/{str(dt_str)}.png')
    
    sleep(10)
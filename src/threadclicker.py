import threading
import random
import time
import pyautogui
import signal
from pynput import keyboard
from pynput.keyboard import Listener
from datetime import datetime

current_time = datetime.now()
exit_event = threading.Event()

def on_press(key):
    if key == keyboard.Key.esc:
        print("Key pressed: {0}".format(key))
        exit_event.set()
        return False #stops listener

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 

def autoclk(n):
    x = random.choice([3,4,5])
    for _ in range(x):
        y = random.choice([1,1.25,1.5])
        pyautogui.click()
        time.sleep(y)
    time.sleep(n)

def simulatedPerson():
    return random.choice([0.5,1.5,1.75,2,2.5,3.5,5])

    
def func():
    t0 = time.time()
    run = True
    print("Start Time: ", current_time.strftime("%H:%M:%S"))
    while run:
        for _ in range(60):
            if time.time() - t0 > 1800*3 or exit_event.is_set():
                run = False
                break
            autoclk(simulatedPerson())
        if run: 
            print("Taking a break @ ", datetime.now().strftime("%H:%M:%S"))
            time.sleep(random.choice([10,15,20,45,60]))
            print("Resuming @ ", datetime.now().strftime("%H:%M:%S"))
        else:
            print('Script Ended: Time Elapsed - ' + convert(time.time() - t0) + " ending @ " + datetime.now().strftime("%H:%M:%S"))
        
        
if __name__ == '__main__':
    print("Waiting 5 seconds before starting ...")
    time.sleep(5)
    
    #auto clicker thread
    x = threading.Thread(target=func)
    x.start()

    with Listener(on_press=on_press) as listener:
        listener.join() #returning false stops listener
    x.join()
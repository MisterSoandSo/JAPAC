#Where Am I Clicking At?
import threading
import pyautogui
from pynput import keyboard, mouse
from pynput.keyboard import Listener

exit_event = threading.Event()

def on_click(x,y,button,pressed):
    if exit_event.is_set(): return False
    if pressed:
        print('Mouse clicked at ({0}, {1})'.format(x, y))

def on_press(key):
    if key == keyboard.Key.esc:
        print("Escape key detected. Ending Script.")
        exit_event.set()
        return False #stops listener

if __name__ == '__main__':
    print("Where Am I Clicking At? has started. Press Esc key and right click to end script.")
    esc_KeyListener = keyboard.Listener(on_press=on_press)
    esc_KeyListener.start()

    with mouse.Listener(on_click=on_click) as ls:
        ls.join()
    
   
    
    
import pyautogui
import time as ts

def main():
    print("Script will now start autoclicking ...")
    try:
        while True:
            # Auto clicker will wait 1 second per click
            pyautogui.click()
            ts.sleep(1)
    except KeyboardInterrupt:
        print('Interrupted: Script ended by user')
if __name__ == '__main__':
    print("Waiting 5 seconds before starting ...")
    ts.sleep(5)
    main()
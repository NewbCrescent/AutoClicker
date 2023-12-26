import pynput
import threading
import keyboard
from time import sleep

delay_time = 0.00001 #for some reason, having a small number like 0.00001 is faster than 0
hotkey_start = "g" #Both hotkeys can't be the same
hotkey_end = "f"


def auto_clicker(stop, delay):
    mouse = pynput.mouse.Controller()

    try:
        while not stop.is_set():
            mouse.press(pynput.mouse.Button.left)
            mouse.release(pynput.mouse.Button.left)
            sleep(delay)

    except KeyboardInterrupt:
        pass


def main():

    stop_autoclicker = threading.Event()
    thread = threading.Thread(target=auto_clicker, args=(stop_autoclicker, delay_time,))

    keyboard.add_hotkey(hotkey_start, thread.start)
    keyboard.wait(hotkey_end)
    stop_autoclicker.set()
    thread.join()


if __name__ == "__main__":
    main()

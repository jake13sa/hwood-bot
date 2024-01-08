import time
from pywinauto.application import Desktop, Application
import keyboard

app = Application(backend="uia").connect(title="Heartwood Online")
window = app.window(title="Heartwood Online")

running = True
paused = False

def press_e():
   keyboard.press("E")
   time.sleep(0.07)
   keyboard.release("E")

def handle_keys():
   global running, paused
   while running:
       if keyboard.is_pressed("B"):
           paused = not paused
           if paused:
               print("Program paused. Press B to resume.")
           else:
               print("Program resumed.")
       elif keyboard.is_pressed("Esc"):
           running = False
           print("Program stopped.")
       time.sleep(0.1)

# Start a separate thread to handle key presses
import threading
keyboard_thread = threading.Thread(target=handle_keys)
keyboard_thread.start()

while running:
   if window.is_active() and not paused:
       press_e()
       time.sleep(0.3)  # Delay between key presses
   else:
       time.sleep(0.1)  # Check for window focus and pause state more frequently

# Wait for the keyboard thread to finish
keyboard_thread.join()

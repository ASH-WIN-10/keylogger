from pynput import keyboard

def on_press(key):
    try:
        print(key.char)
    except AttributeError:
        if key == keyboard.Key.esc:
            # Stop listener
            return False

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
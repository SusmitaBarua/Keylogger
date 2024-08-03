#from pynput.mouse import controller
from pynput.keyboard import controller
# left to right, top to bottom
#from top-left of the screen you can imagine the top-left to be (0,0)
def controlMouse():
    mouse = controller()
    mouse.position = (500,200)

def controlKeyboard():
    keyboard = controller()
    keyboard.type("it should work")

controlKeyboard()
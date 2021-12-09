from pynput.mouse import Button, Controller




activated = False

mouse = Controller()  

human_input = input("Activate system control? (Y/n) ")
raw_input = raw_input("Press Enter to continue...")

if human_input == "n":
    activated = False
else:
    activated = True

while activated:
    # Read pointer position
    print('The current pointer position is {0}'.format(mouse.position))

def move(target_x, target_y):

    # Set pointer position
    mouse.position = (target_x, target_y)
    print('Now we have moved it to {0}'.format(mouse.position))

    # Move pointer relative to current position
    mouse.move(5, -5)

    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

    # Double click; this is different from pressing and releasing
    # twice on Mac OSX
    mouse.click(Button.left, 2)

    # Scroll two steps down
    mouse.scroll(0, 2)

    """
    exit 1
    Echo
    """



# def get_context()
    


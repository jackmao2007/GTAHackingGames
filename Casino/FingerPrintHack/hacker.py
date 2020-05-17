import time
import directKeys

HACK_ORDER = ["NONE", "DOWN", "DOWN", "DOWN", "RIGHT", "UP", "UP", "UP"]

def move_selection(command):
    """ Moves the selected the option according to command
    """
    if command == "DOWN":
        directKeys.PressKey(0xD0)  # press down
        time.sleep(0.05)
        directKeys.ReleaseKey(0xD0)
    elif command == "UP":
        directKeys.PressKey(0xC8)  # press up
        time.sleep(0.05)
        directKeys.ReleaseKey(0xC8)
    elif command == "RIGHT":
        directKeys.PressKey(0xCD)  # press right
        time.sleep(0.05)
        directKeys.ReleaseKey(0xCD)
    elif command == "LEFT":
        directKeys.PressKey(0xCB)  # press left
        time.sleep(0.05)
        directKeys.ReleaseKey(0xCB)
    # else command is "NONE", do nothing
    time.sleep(0.05)


def confirm_option(is_solution):
    """ Press enter to confirm the finger print option if is_solution is true
    """
    if is_solution:
        directKeys.PressKey(0x1C)  # press enter
        time.sleep(0.05)
        directKeys.ReleaseKey(0x1C)
    time.sleep(0.05)


def confirm_solution():
    """ Finish the hacking by pressing tab"""
    directKeys.PressKey(0x0f)  # press tab
    time.sleep(0.05)
    directKeys.ReleaseKey(0x0f)
    time.sleep(4.0) # wait for next pattern


def begin_hack(solution):
    """ Hack the finger print machine using the given solution to each finger print option
    """
    for i in range(len(HACK_ORDER)):
        move_selection(HACK_ORDER[i])
        confirm_option(solution[i])
    confirm_solution()


if __name__ == "__main__":
    a = [False, False, False, False, True, True, True, True]
    time.sleep(1)
    begin_hack(a)

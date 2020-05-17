import cv2
import numpy as np
from PIL import ImageGrab
import win32gui


def find_gta_window_pos():
    """ Finds the window where gta game is on.
        Returns the positions of the game
    """
    # Detect the window with GTA
    game_hwnd = win32gui.FindWindow(None, "Grand Theft Auto V")
    game_pos = win32gui.GetWindowRect(game_hwnd)
    return game_pos


def grab_gta_screen(game_pos):
    """ Takes the current screen of the game
        Returns a BRG image in a array
    """
    screen_shot = ImageGrab.grab(game_pos)
    screen_shot = np.array(screen_shot)
    screen_shot = cv2.cvtColor(screen_shot, cv2.COLOR_RGB2BGR)
    return screen_shot


def grab_finger_print(screen_shot):
    """ Takes the current displayed finger print on the screen
        Returns a BRG image in a array
    """
    topleft_factor = (0.14583333333333334, 0.4625)
    bottomright_factor = (0.6319444444444444, 0.73828125)

    size = screen_shot.shape
    x = (int(topleft_factor[0]*size[0]), int(bottomright_factor[0]*size[0]))
    y = (int(topleft_factor[1]*size[1]), int(bottomright_factor[1]*size[1]))
    return screen_shot[x[0]:x[1], y[0]:y[1]]


def grab_finger_print_fragment_options(screen_shot):
    """ Takes each finger print option to select and return them in a list
    from top to down to right then back up. in index of list will be like:

    0 7
    1 6
    2 5
    3 4
        Returns a list of BRG images
    """
    option_box_factor = (0.1111111111111111, 0.0625)
    column_y_factors = [0.24609375, 0.32109375]
    row_x_factors = [0.24861111111111112, 0.3819444444444444, 0.5152777777777777, 0.6486111111111111]

    size = screen_shot.shape
    option_box_size = (int(option_box_factor[0]*size[0]), int(option_box_factor[1]*size[1]))
    column = [int(factor_y * size[1]) for factor_y in column_y_factors]
    row = [int(factor_x * size[0]) for factor_x in row_x_factors]
    # (x-start, x-end, y-start, y-end)
    opt0 = screen_shot[row[0]:row[0]+option_box_size[0], column[0]:column[0] + option_box_size[1]]
    opt1 = screen_shot[row[1]:row[1]+option_box_size[0], column[0]:column[0] + option_box_size[1]]
    opt2 = screen_shot[row[2]:row[2]+option_box_size[0], column[0]:column[0] + option_box_size[1]]
    opt3 = screen_shot[row[3]:row[3]+option_box_size[0], column[0]:column[0] + option_box_size[1]]
    opt4 = screen_shot[row[3]:row[3]+option_box_size[0], column[1]:column[1] + option_box_size[1]]
    opt5 = screen_shot[row[2]:row[2]+option_box_size[0], column[1]:column[1] + option_box_size[1]]
    opt6 = screen_shot[row[1]:row[1]+option_box_size[0], column[1]:column[1] + option_box_size[1]]
    opt7 = screen_shot[row[0]:row[0]+option_box_size[0], column[1]:column[1] + option_box_size[1]]
    finger_print_options = [opt0, opt1, opt2, opt3, opt4, opt5, opt6, opt7]
    return finger_print_options


if __name__ == "__main__":
    # pos = find_gta_window_pos()
    # print(pos)
    # image = grab_gta_screen(pos)
    image = cv2.imread("test.jpg")
    # print(image.shape)
    image2 = grab_finger_print(image)
    image3 = grab_finger_print_fragment_options(image)
    # cv2.imwrite("test.jpg", image)
    cv2.imwrite("testPrint.jpg", image2)
    i = -1
    for im in image3:
        i += 1
        cv2.imwrite("testoption"+str(i)+".jpg", im)

    # cv2.imshow("Screen", image2)
    # cv2.waitKey(0)
    #
    # topleft = (80/1280, 80/720)
    # bottomright = (945/1280, 455/720)
    #
    # print(topleft)
    # print(bottomright)

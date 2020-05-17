import cv2
import numpy as np
import os

MIN_PRINT_MATCH_THRESHHOLD = 60000000
MIN_OPTION_MATCH_THRESHOLD = 15000000
MATCHING_METHOD = "cv2.TM_CCOEFF"


def match_finger_print_to_templates(finger_print):
    """ Match the given finger_print to the templates and return the correct solution
        Returns an image in a array that is the template for the given finger_print
        Returns None if the matching score is below threshold (did not match any templates)
    """
    max_cor = 0
    max_template = None
    finger_print = cv2.resize(finger_print, (530, 530))
    finger_print = cv2.cvtColor(finger_print, cv2.COLOR_BGR2GRAY)
    for template_name in os.listdir("cheatSheet"):
        if template_name == "fullSheet.jpg":
            continue
        template = cv2.imread("cheatSheet/"+template_name)
        method = eval(MATCHING_METHOD)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(template, finger_print, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > MIN_PRINT_MATCH_THRESHHOLD and max_val > max_cor:
            max_cor = max_val
            max_template = template
    return max_template


def match_finger_print_options_to_template(finger_print_options, template):
    """ Match each option in finger_print_options to the template and return if the
    option is correct
        Return a list of boolean values parallel to finger_print_options indicating the
    right choices
    """
    method = eval(MATCHING_METHOD)
    result = [False, False, False, False, False, False, False, False]
    for i in range(len(finger_print_options)):
        option = cv2.resize(finger_print_options[i], (110, 110))
        option = cv2.cvtColor(option, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(template, option, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > MIN_OPTION_MATCH_THRESHOLD:
            result[i] = True
    return result


if __name__ == "__main__":
    test_print = cv2.imread("testPrint.jpg")
    test_print_options = []
    for i in range(8):
        test_print_options.append(cv2.imread("testoption"+str(i)+".jpg"))
    templ = match_finger_print_to_templates(test_print)
    res = match_finger_print_options_to_template(test_print_options, templ)
    print(res)
import Casino.FingerPrintHack.imageProcessor as ip
from Casino.FingerPrintHack import templateMatcher as tm
from Casino.FingerPrintHack import hacker as hr
import time
import win32api

activation = False
MAX_HACK_COUNT = 1
count = 0
while True:
    if win32api.GetAsyncKeyState(0x73) or count == MAX_HACK_COUNT:  # press F4 to activate
        activation = not activation
        print('activated' if activation else 'deactivated')
        time.sleep(0.2)
        count = 0
    if activation:
        pos = ip.find_gta_window_pos()
        image = ip.grab_gta_screen(pos)
        test_print = ip.grab_finger_print(image)
        test_print_options = ip.grab_finger_print_fragment_options(image)

        templ = tm.match_finger_print_to_templates(test_print)
        if templ is None: # no matching template
            time.sleep(2)
            continue
        res = tm.match_finger_print_options_to_template(test_print_options, templ)

        hr.begin_hack(res)

        count += 1

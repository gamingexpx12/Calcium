from tkinter import *

from typing import List

import tkhelper


def test_buttonsfrom_dict_one_input_value() -> None:
    def testHandler(e: Event) -> None:
        pass

    root = Tk()
    dict: tkhelper.callbackDict = {"1" : testHandler, "2" : testHandler}
    buttons = tkhelper.buttons_from_dict(dict, root)
    print(buttons)

    assert type([]) is list

    assert(type(buttons) is list), (
        "buttons_from_dict did not return a list of buttons!")



def runtests() -> None:
    test_buttonsfrom_dict_one_input_value()
    print("All tests succeded")


if __name__ == '__main__':
    runtests()

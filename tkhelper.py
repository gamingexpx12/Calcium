from typing import Dict, List, Callable, Any


from tkinter import *


callback = Callable[[Event], None]
callbackDict = Dict[str, callback]

def buttons_from_dict(dict_: callbackDict, parent: Tk) -> List[Button]:
    buttons: List[Button] = []
    for name, callback in dict_.items():
        buttons.append(Button(parent, text = name))

    return buttons

def one_handler(event: Event) -> None:
    print("ONE")

if __name__ == '__main__':
    pass

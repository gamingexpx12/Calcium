import math


from tkinter import *

root = Tk()
root.tile = "Calcium"
mainContainer = Frame(root).grid()

windowContainer = Frame(mainContainer).grid(row = 0)


def standardButton(name, container, click1_handler, row = 0, column = 0):
    """Creates, binds and packs a button with the desired name, handler"""

    button = Button(container)
    button["text"] = name
    button.bind("<Button-1>", click1_handler)
    button.bind("<Return>", click1_handler)
    button.grid(row = row, column = col)

def a_handler(event):
    print(event.widget["text"])

buttonContainer = Frame(mainContainer).grid(row = 0)

row_width = 3
for index in range(10):
    row = math.floor(index / row_width)
    col = index % row_width
    standardButton(index, buttonContainer, a_handler,
                    row = row,
                    column = col)
root.mainloop()

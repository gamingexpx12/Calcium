from tkinter import *


class CalciumApp:
    def layout(self: CalciumApp) -> None:
        self.results = Label(self.root, text ="Results")
        self.results.grid(column = 0, row = 0, columnspan = 3)

        self.button1 = Button(self.root, text = "1")
        self.button1.grid(column = 0, row = 1)

        self.button2 = Button(self.root, text = "2")
        self.button2.grid(column = 1, row = 1)

        self.button3 = Button(self.root, text = "3")
        self.button3.grid(column = 2, row = 1)


    def __init__(self: CalciumApp, root: Tk) -> None:
        self.root = root
        self.layout()


    def run(self: CalciumApp) -> None:
        mainloop()


def main() -> None:
    root = Tk()
    app = CalciumApp(root)
    app.run()


if __name__ == '__main__':
    main()

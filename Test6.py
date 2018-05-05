"""
Moved all logic into a decision object which can be reused.
"""
from tkinter import *


class Choice:
    def __init__(self, description_text, keyword, handler_func):
        self.description_text = description_text
        self.keyword = keyword
        self.handler_func = handler_func

class Decision:
    def __init__(self, choices, decision_text = ""):
        self.choices = choices
        self.decision_text = decision_text

    def add_choice(self, choice):
        choices.append(choice)

    def response_handler(response):
        for choice in self.choices:
            if choice.keyword == response:
                choice.handler_func()
                break
        else:
            handle_default()

    def ask(self):
        root = Tk()
        desc_container = Frame(root)
        desc_container.pack()
        desc = Label(root, text=self.decision_text)
        desc.pack()

        answer_container = Frame(root)
        answer_container.pack()

        for choice in self.choices:
            butt = Button(root, text=choice.description_text)
            butt.bind("<Button-1>", choice.handler_func)
            butt.pack(side=RIGHT)

        root.mainloop()




def handle_A(event):
    print("Quite!")

def handle_B(event):
    print("Nope")

def handle_C(event):
    print("Are you mad?")

def handle_default(event):
    print("Choice not recognized, try again.")

def handle_correct(event):
    print("That's correct!")

def handle_incorrect(event):
    print("NOPE!")

choices = [
    Choice("Flown in on north-african swallows", "A", handle_A),
    Choice("Shipped from West-Germany", "B", handle_B),
    Choice("Dropped by domesticated killer bunnies", "C", handle_C),
]



def printChoices(iter_of_choices):
    for choice in iter_of_choices:
        print("{0} : {1}".format(choice.keyword, choice.description_text))

def main():
    decision = Decision(decision_text = "Who started world war two?",
    choices = [
        Choice("Germany", "DE", handle_correct),
        Choice("France", "FR", handle_incorrect),
        Choice("Poland", "PL", handle_incorrect),
    ]).ask()

if __name__ == '__main__':
    main()

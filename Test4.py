"""
Added else statement to response checking, if input was not valid.
"""

class Choice:
    def __init__(self, description_text, keyword, handler_func):
        self.description_text = description_text
        self.keyword = keyword
        self.handler_func = handler_func

def handle_A():
    print("Quite!")

def handle_B():
    print("Nope")

def handle_C():
    print("Are you mad?")

def handle_default():
    print("Choice not recognized, try again.")

choices = [
    Choice("Flown in on north-african swallows", "A", handle_A),
    Choice("Shipped from West-Germany", "B", handle_B),
    Choice("Dropped by domesticated killer bunnies", "C", handle_C),
]

def printChoices(iter_of_choices):
    for choice in iter_of_choices:
        print("{0} : {1}".format(choice.keyword, choice.description_text))

def main():
    print(
    "=" * 70,
    "How did coconuts first come to England?",
    "=" * 70,
    sep="\n"
    )
    printChoices(choices)
    print(
    "=" * 70,
    sep="\n"
    )

    response = input("Your answer: ").upper()

    for choice in choices:
        if choice.keyword == response:
            choice.handler_func()
            break
    else:
        handle_default()

if __name__ == '__main__':
    main()

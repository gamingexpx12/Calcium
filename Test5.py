"""
Moved all logic into a decision object which can be reused.
"""

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

    def ask(self):
        print(
        "=" * 70,
        sep="\n"
        )

        print(self.decision_text)

        print(
        "=" * 70,
        sep="\n"
        )
        printChoices(self.choices)
        print(
        "=" * 70,
        sep="\n"
        )

        response = input("Your answer: ").upper()

        for choice in self.choices:
            if choice.keyword == response:
                choice.handler_func()
                break
        else:
            handle_default()

def handle_A():
    print("Quite!")

def handle_B():
    print("Nope")

def handle_C():
    print("Are you mad?")

def handle_default():
    print("Choice not recognized, try again.")

def handle_correct():
    print("That's correct!")

def handle_incorrect():
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

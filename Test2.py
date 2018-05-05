"""
Made choices into a dictionary to seperate data and code for easy editing. Choice text is still added in code.
"""

def handle_A():
    print("Quite!")

def handle_B():
    print("Nope")

def handle_C():
    print("Are you mad?")

def handle_default():
    print("Choice not recognized, try again.")

choices = {
    "A" : handle_A,
    "B" : handle_B,
    "C" : handle_C
    }

def main():
    print(
    "=" * 70,
    "How did coconuts first come to England?",
    "=" * 70,
    "A: Flown in on african swallows",
    "B: Shipped from East-Germany",
    "C: Dropped by wild killer bunnies",
    "=" * 70,
    sep="\n"
    )

    response = input("Your answer: ").upper()

    action = choices.get(response, handle_default)
    action()

if __name__ == '__main__':
    main()

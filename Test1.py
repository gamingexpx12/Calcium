def handle_A():
    print("Quite!")

def handle_B():
    print("Nope")

def handle_C():
    print("Are you mad?")

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

    if response == "A": handle_A()
    if response == "B": handle_B()
    if response == "C": handle_C()

if __name__ == '__main__':
    main()

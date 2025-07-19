def _interactive_greeting():
    name = input("What is your name? \n")
    if name == "":
        print(f'Type a real name \n')
        name = input("Type a real name Now : \n")
    else:
        print(f'Hello World {name} it is a pleasure to meet you !\n')

_interactive_greeting()
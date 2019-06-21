# THIS IS A SNAKE, WATER, GUN GAME MADE BY VED
import random
print("Welcome to SNAKE, WATER, GUN, a GAME Created By Ved.")
print("This is a Choice game.")
print('''Rules:
1: Select your Choice one at a time.
2: You have 11 chances to beat computer.
3: You can quit anytime just by typing exit.  ''')

Value = {}
i = 1
c_user = c_comp = 0
l = ['s', 'w', 'g']
z = 'y'
while z == 'y':
    while i <= 11:
        print("Choices avaliable:", l)
        choice = input("Enter your choice: ").lower()
        if choice == 'exit':
            break
        elif 's' in choice:
            pass
        elif 'w' in choice:
            pass
        elif 'g' in choice:
            pass
        else:
            print("Retry")
            continue

        comp_choice = random.choice(l)
        Value[i] = [choice, comp_choice]
        i += 1

        if choice == comp_choice:
            continue
        elif choice == 's':
            if comp_choice == 'w':
                c_user += 1
            else:
                c_comp += 1
        elif choice == 'w':
            if comp_choice == 's':
                c_comp += 1
            else:
                c_user += 1
        else:
            if comp_choice == 's':
                c_user += 1
            else:
                c_comp += 1

    print("Player Scored:", c_user)
    print("Computer Scored:", c_comp)
    print("Score Card:", Value)
    if c_user > c_comp:
        print("Player WINS")
    elif c_user < c_comp:
        print("Computer WINS")
    else:
        print("IT WAS A TIE")
    z = input('Want To Play Again? y/n: ')
    i = 1
    c_user = c_comp = 0
Endline = input("Press Enter to Exit")

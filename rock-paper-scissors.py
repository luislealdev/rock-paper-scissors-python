import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userChoice = int(input('Write:\n"0" for Rock\n"1" for paper\n"2" for scissors\nEnter: '))

if(userChoice == 0 or userChoice == 1 or userChoice == 2):
    options = [rock, paper, scissors]
    print(options[userChoice])

    computerChoice = random.randint(0,2)
    print("Computer choise: \n" + options[computerChoice])

    if(userChoice==computerChoice):
        print("IT'S A TIE")
    elif((userChoice==0 and computerChoice==1) or (userChoice==1 and computerChoice==2)):
        print("COMPUTER WON ;(")
    elif((userChoice==1 and computerChoice==0) or (userChoice==2 and computerChoice==1)):
        print("¡¡YOU WON!!")
else:
    print("Invalid number")
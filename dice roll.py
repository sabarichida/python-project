import random
def RollDice(rolls):
  for i in range(0, rolls):
    number = random.randint(1,6)
    print("---")
    print("-"+ str(number)+"-")
    print()
  Menu()
def Menu():
    print("1. ROll a Dice")
    print("2. Roll multiple Dice")
    print("----------------------")
    print("3. Exit program")
    print()
    choice = int(input("Enter here:"))  

    if (choice == 1):
       RollDice(1)
    if (choice == 2):
       rolls = int(input("How many rolls?"))
       RollDice(rolls)
    if(choice == 3):
       exit();
Menu()             
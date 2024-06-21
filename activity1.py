#library
from random import randint
#randint loop 3 times
Random_numbers = [randint(0,9) for i in range(3)]
#assign the randit to variables and convert from list to str i use map to apply str fucntion to the elements
result = ''.join(map(str , Random_numbers))
#userinput
UserBet = input("Enter 3 Number: ")

#validation of inputs and results
if len(UserBet) == 3 and UserBet.isdigit():
    print(f"Your combination - {UserBet} Result - {result} ")
    print("You win" if UserBet == result else  "Partial win " if sorted(UserBet) == sorted(result) else "You Lose!" )
else:
    print("Please input Number Only" if not UserBet.isdigit() else "input 3 numbers only ")
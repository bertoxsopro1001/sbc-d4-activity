#library
from random import randint
#randint loop 2 times
Random = [randint(0,1) for i in range(2)]

#use  the number as a key to be easy to identify the value  nested dictionary
choice = {"digit":{"fold" : 0,"unfold":1}, "number" :{0:"fold",1:"unfold"}}

#assinging cp 1 and cp2 for randint
computer_1,computer_2 = Random

Player_1 = input("Enter Choice: Fold - Unfold ").lower()

#validation
if Player_1.isalpha():
   #using boolean value for validate the winner
   print(f" \n Player1 : {Player_1} \n Computer1 : {choice['number'][computer_1]} \n Computer2 {choice['number'][computer_2]}")
   GameResult = (
    "Player 1 wins" if (computer_1 * computer_2 == 0) * (choice["digit"][Player_1] == 1)
    else "Player 1 wins" if (computer_1 * computer_2 == 1) * (choice["digit"][Player_1] == 0)
    else "Computer 2 wins" if (computer_1 * choice["digit"][Player_1] == 0) * (computer_2 == 1)
    else "Computer 2 wins" if (computer_1 * choice["digit"][Player_1] == 1) * (computer_2 == 0)
    else "Computer 1 wins" if (computer_2 * choice["digit"][Player_1] == 0) * (computer_1 == 1)
    else "Computer 2 wins" if (computer_2 * choice["digit"][Player_1] == 1) * (computer_1 == 0)
    else "Draw"
)
   
   print(GameResult)


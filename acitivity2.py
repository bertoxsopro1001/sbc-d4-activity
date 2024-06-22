from random import randint
while True:
    # Dictionary to convert number to word
    text_convert = {0: "fold", 1: "unfold"}
    # Assign random choices for computers
    computer_1, computer_2 = [randint(0, 1) for _ in range(2)]
    # User input
    Player_1 = input("Enter 0 - fold, 1 - unfold : ")
   #input validation
    if  Player_1.isdigit() and Player_1 in ['0', '1']:
         Player_1 = int(Player_1)
         print(f"Player 1 - {text_convert[Player_1]}\nComputer 1 - {text_convert[computer_1]}\nComputer 2 - {text_convert[computer_2]}\n"
          f"{'Player 1 win' if (computer_1 != Player_1) & (computer_2 != Player_1) else 'Computer 1 win' if (Player_1 != computer_1) & (computer_2 == Player_1) else 'Computer 2 win' if (Player_1 != computer_2) & (computer_1 == Player_1) else 'Draw'}")
         
    else: print("0 for fold, 1 for unfold" if Player_1.isalpha() else "Invalid input")


  

import random
continue_game=True
while(continue_game):
    user_choice=int(input("\n0 for rock\n1 for paper\n2 for scissor\nEnter your choice:"))
    print(f"you chose {user_choice}: ")
    if user_choice<0 or user_choice>=3:
        print("invalid choice")
    else:
        computer_choice=random.randint(0,2)
        print("computer chose:",end=" ")
        print(computer_choice)
        if computer_choice==user_choice:
            print("It's a draw.")
        elif computer_choice==0 and user_choice==2:
            print("you lose.")
        elif user_choice==0 and computer_choice==2:
            print("you win.")
        elif computer_choice>user_choice:
            print("you lose.")
        elif user_choice>computer_choice:
            print("you win.")
    x=input("Continue the game(yes/no)? ")
    if x=="no":
        continue_game=False

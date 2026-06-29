import random

choices = ["rock","paper","scissors"]

user_score = 0
computer_score = 0

while True :

    user = input("\nEnter your choice (Rock, Paper or Scissors) :").lower()

    if user not in choices :
        print("Invalid Choice!")
        continue

    computer = random.choice(choices)

    print(f'You chose : {user}')
    print(f'Computer chose : {computer}')

    if (user == computer) :
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") :
        print("You Win!")
        user_score+=1
    
    elif (user == "paper" and computer == "rock") :
        print("You Win!")  
        user_score+=1

    elif (user == "scissors" and computer == "paper") :
        print("You Win!")
        user_score+=1

    else :
        print("Computer Wins!")
        computer_score+=1

    again = input("\n Wanna Play Again? (Yes/No) :").lower()

    if again == "no":
        print("\nFinal Score :")
        print(f'Your Score : {user_score}')
        print(f'computer Score : {computer_score}')
        print('''Thanks For playing! 
        See you soon...''')
        break






           
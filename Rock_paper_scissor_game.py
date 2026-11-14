import random


print("Welcome To Sadiq Rock-Paper-Scissors!\n")
print("Wining Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Sicssors Wins\n")

choices =["Rock", "Paper","Scissors"]

while True:

    print("Choose an option:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    try:
        choice = int(input("Enter your Choice: "))
    except ValueError:
        print("Please enter a Valid number.\n")
        continue

    while choice <1 or choice > 3:
        choice = int(input("Please enter a Valid choice (1-3):"))

    user_choice=choices[choice -1]

    print("\nUser choice iss:", user_choice)
    print("Now it's Computer's Turn...")

    comp_choice= random.randint(1,3)
    computer_choice= choices[comp_choice - 1]

    print("Computer choice is:", computer_choice)
    print(user_choice, "VS", computer_choice)


    if choice == comp_choice:
        print("** It's a Tie! **")

    elif (
        (choice == 1 and comp_choice == 3) or
        (choice == 2 and comp_choice == 1) or
        (choice == 3 and comp_choice == 2)
    ):
        print("** User Wins! **")
    else:
        print("** Computer Wins! **")

    while True:
        ans = input("\n Do you want To play again? (Y/N):").lower()

        if ans in ['y' , 'n']:
            break
        print("Please enter Y Or N.")

    if ans == 'n':
        break
    print()

    print("/n Thanks fro Playing Sadiq Game")
import random  #To generate a random number
name = input("Please Enter your name: ")
print("Welcome to my Number game, " + name)
def intro():
    number = random.randint(1,200)   #Generates a random number
    print("\nI have selected a number between 1 to 200...")
    print("You have 6 chances to guess that number...")
    i = 1
    r = 1
    while i<7:  #6 Chances to the user
        u_guess = int(input('Enter your number: ')) 
        if u_guess < number:
            print(" My number is greater than your guessed number")
            print("you now have " + str(6-i)+ " chances left" )
            i = i+1
        elif u_guess > number:
            print(" My number is less than your guessed number")
            print("you now have " + str(6-i)+ " chances left" )
            i = i+1
        elif u_guess == number:
            print("\nCongratulations "+name+"!! You have guessed the correct number!")
            r = 0;
            break
        else:
            print("This is an invalid number. Please try again")
            print("you now have " + str(6-i)+ " chances left" )
            continue
    if r==1:
        print("Sorry you lost the game!!")
        print("My number was = " + str(number))

def main():
    intro()
    while True:
        another_intro = input("Do you wish to play again?(y/n): ")
        if another_intro == "y":
            intro()
        else:
            break
main()
print("\nEnd of the Game! Thank you for playing!")

import random

guess_taken = 0

number = random.randint(1, 9)

print("Please what is your name? ")
myName = input()

print()
print(f"Well { myName } think of a number between 0 and 21")
print()
while guess_taken < 6:

    # print("Guess a number: ")
    # guess = input()
    # guess = int(guess)
    guess = int(input("Guess a number: "))
    
    guess_taken += 1

    if guess < number:
        print("Your guess is low! ")

    if guess > number:
        print("Your guess is high! ")    

    if number == guess:
        break

print()

if number == guess:
    print(f"Congratulation! {myName} you have been able to guess the correct number! ")

if number != guess:
    number = str(number)
    print(f"Sorry {myName} you couldn't guess the correct nunber! ")  
    print()
    print(f"The correct answer: {number}")     
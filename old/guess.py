import random



answer = random.randrange(1, 10)

correct = False

num = 3

for i in range(3):

    guess = int(input("Enter any number from 1 to 10: "))

    if guess < answer:

        print("Too low!")
        num = num - 1
        print(num)        
        print("guesses are left")

    elif guess > answer:

        print("Too high!")
        num = num - 1
        print(num)
        print("guesses are left")
    else:

        print("You guessed it right!!")

        correct = True

        break



if correct is False:

    print("Sorry, you lost!")
    print(answer)
    print("was the answer.")
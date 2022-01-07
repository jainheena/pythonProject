import random
winning_no = random.randint(1, 3)
user_input = int(input("enter a number "))
if winning_no == user_input:
    print("congratulations! you won.")
else:
    print("Oops! You lost")
    print("Your winning no. is :", winning_no)




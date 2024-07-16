# This program s going to request for a number from the between the range of 1-10
# The program then picks a random number and compares it to the users input and then outputs a result
import random

try:
    user_input = int(input("Enter Number between 1-10: "))
except ValueError:
    print("This game only accepts integer values between 1-10\n try again")
random_num = random.randint(1,10)
def main():    
    if user_input == random_num:
        print("CONGRATULATIONS!!! YOU GUESSED RIGHT.")
        print(f"You: {user_input} || Computer: {random_num}")
    elif (user_input == random_num-1) | (user_input == random_num-2) | (user_input == random_num+2) | (user_input == random_num+1):
        print("OOOH! You almost had it, try again")
        print(f"You: {user_input} || Computer: {random_num}")

    else:
        print("OHH Wrong!! You are far from home, try again you might win")
        print(f"You: {user_input} || Computer: {random_num}  {random_num+1}")

try:
    if __name__ == "__main__":
        main()
except NameError:
    pass
# The program is going to utilize Regular Expressions to validate an email input
import re
userInput = input("Type 'email' to check your Email validity or type 'tweet' to check your twitter username: ")

def email():
    email_address = input("Enter Email address: ").strip()
    if re.search(r"^\w+@\w+\.(com|edu|org|biz)$", email_address,re.IGNORECASE) :
        print(f"{email_address} is a valid email address")
    else:
        print("Invalid email address, retry")

def twitter_url():
    user = input("Enter your Twitter Url: ").strip()
    user_name = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", user, re.IGNORECASE)
    if user_name:
        print(f"Your username is: {user_name.group(3)}")
    else:
        print("It is invalid")

if userInput == 'email':
    email()

elif userInput == 'tweet':
    twitter_url()

else:
    print("wrong input, read instrution and try again")

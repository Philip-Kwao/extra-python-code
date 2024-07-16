# This file is going to contain a squared function that will be used for testing

def main():
    sqNum = int(input("What is the Number: "))
    print(f"The squared value is: {sqFun(sqNum)}")

def sqFun(num):
    return num+num

 
if __name__ == "__main__":
    main()
# I am going to test the squared function in this file

from squareFunc import sqFun

def test_main():
    test_sqFunc()

def test_sqFunc():
    # if sqFun(2) != 4:
    #     print("The squared of 2 is not 4")
    # if sqFun(3) != 9:
    #     print("The square of 3 is not 9") 
    try:
        assert(sqFun(2))==4
    except AssertionError:
        print("The squared of 2 is not 4")
    try:
        assert(sqFun(3))==9
    except AssertionError:
        print("The squared of 3 is not 9")
    # assert(-2)==4
    # assert(-3)==9
    # assert(0)==0

if __name__ == "__main__":
    test_main()
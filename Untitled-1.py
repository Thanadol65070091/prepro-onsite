"""This is docstring"""
def main():
    """This is docstring"""
    money = int(input())
    water = int(input())
    snac1 = int(input())
    snac2 = int(input())
    snac3 = int(input())
    money1 = money - water
    if money1 % 3 == 0:
        num1 = snac1 * 10
        money1 = money1 - num1
    elif money1 % 3 == 1:
        num1 = snac1 * 15
        money1 = money1 - num1
    elif money1 % 3 == 2:
        num1 = snac1 * 20
        money1 = money1 - num1
    if money1 % 3 == 0:
        num2 = snac2 * 12
        money1 = money1 - num2
    elif money1 % 3 == 1:
        num2 = snac2 * 15
        money1 = money1 - num2
    elif money1 % 3 == 2:
        num2 = snac2 * 18
        money1 = money1 - num2
    if money1 % 3 == 0:
        num3 = snac3 * 5
        money1 = money1 - num3
    elif money1 % 3 == 1:
        num3 = snac3 * 7
        money1 = money1 - num3
    elif money1 % 3 == 2:
        num3 = snac3 * 9
        money1 = money1 - num3
    if money1 < 0:
        print("Now you have %d left." %money)
        print("You don't have enough money!")
    else:
        print("Now you have %d left." %money1)
        print("Here's your order!")
        print("Water: %d baht" %water)
        print("Snack number 1: %d baht" %num1)
        print("Snack number 2: %d baht" %num2)
        print("Snack number 3: %d baht" %num3)
main()

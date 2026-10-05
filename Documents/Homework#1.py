import math
def is_positive_odd():
    print("Give me a number and I will tell you wether it is both greater than zero and odd (True) or not (False)")
    num = float(input())
    if num>0 and num%2 != 0:
        return True
    else:
        return False
    print(result)
def area_of_rectangle():
    print("Give me a length and a width and I will find the area of their rectangle")
    num1=float(input())
    num2=float(input())
    print("The area is ",num1*num2)
def circumference():
    print("Give me a radius and I will find the circumference of that circle")
    num=float(input())
    Constant = 2*math.pi
    print("The circumference is ",num*Constant)
def area_of_circle():
    print("Give me a radius and I will find the area of that circle")
    num=float(input())
    print("The area is ",num*num*math.pi)
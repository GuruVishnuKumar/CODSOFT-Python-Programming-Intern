
import math
def add(a,b):
    a+=b
    return a
def sub(a,b):
    if(a>b):
        a-=b
        return a
    else:
        b-=a
        return b
def mul(a,b):
    a*=b
    return a
def div(a,b):
    q=a/b
    r=a%b
    print("Quotient  ==> %s"%q)
    print("Remainder ==> %s"%r)
def sqr(a):
    c=math.sqrt(a)
    return c
print(".....SIMPLE CALCULATOR.....")
print("\n-----OPERATIONS-----\n")
print("1. Addition\n")
print("2. Subtraction\n")
print("3. Multipilication\n")
print("4. Division\n")
print("5. SquareRoot\n")
print("6. Exit")
while(True):
    choice=int(input("Enter Your Choice\n-->"))
    if(choice==1):
        print("\nEnter Two Numbers\n")
        num1=int(input('-->'))
        num2=int(input('-->'))
        A=add(num1,num2)
        print("\nSum ==> %s"%A)
    elif(choice==2):
        print("\nEnter Two Numbers\n")
        num1=int(input('-->'))
        num2=int(input('-->'))
        B=sub(num1,num2)
        print("\nDifference ==> %s"%B)
    elif(choice==3):
        print("\nEnter Two Numbers\n")
        num1=int(input('-->'))
        num2=int(input('-->'))
        C=mul(num1,num2)
        print("\nProduct ==> %s"%C)
    elif(choice==4):
        print("\nEnter Two Numbers\n")
        num1=int(input('-->'))
        num2=int(input('-->'))
        D=div(num1,num2)
    elif(choice==5):
        print("\nEnter Number\n")
        num1=int(input('-->'))
        E=sqr(num1)
        print("\nSquareRoot ==> %s"%E)
    elif(choice==6):
        print("\n.....ThankYou.....")
        break
    else:
        print("\n*****Invaild Choice*****")
        break
#1.	Write a Python program to convert kilometers to miles?
def KM_Miles():
    try:
        a = int(input("enter the Kms value:"))
        b = a*0.621371
        print("the equivalant value in miles is:",b)
    except Exception as e:
        print(e)
KM_Miles()

#2.	Write a Python program to convert Celsius to Fahrenheit? [32]
def Cel_Far():
    try:
        a = int(input("enter the Celsius value:"))
        b = (a*(9/5))+32
        print("the equivalant value in Fahrenheit is:",b)
    except Exception as e:
        print(e)
Cel_Far()

#3. Write a Python program to display calendar?
try:
    import calendar

    yy = int(input("Enter year: "))
    mm = int(input("Enter month: "))

    print(calendar.month(yy, mm))
except Exception as e:
    print(e)

#4. Write a python program to solve a quadratic equation?

def quad_solve():
    print("Enter the values of constants of the quadratic equation of form ax2 + bx +c =0")
    try:
        a = int(input("enter value of a"))
        b = int(input("enter value of b"))
        c = int(input("enter value of c"))
    except Exception as e:
        print(e)
    import cmath
    try:
        d = ((b**2) - (4*a*c))
        D = cmath.sqrt(d)
        x1 = (((-b)+D)/(2*a))
        x2 = (((-b)-D)/(2*a))

        print("Solution x1 is :", round(x1.real,2)+round(x1.imag,2)*1j)
        print("Solution x2 is :", round(x2.real,2)+round(x2.imag,2)*1j)
    except Exception as e:
        print(e)
quad_solve()

#5. Write a Python program to swap two variables without temp variable?

a = 10
b = 5
a,b=b,a
print("value of a is :",a," , ","value of b is :",b)


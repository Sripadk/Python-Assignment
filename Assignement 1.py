#Q1:
print("Hello Python")

#Q2
a= 10
b = 20
print(a+b)
print(b/a)

#Q3
# b = base of triangle, h = height of triangle, A = area of triangle
h = 0
b = 0
try:
    h= int(input("enter the height of the triangle: "))
    b =int(input("enter the base length of the triangle: "))
    print("area of triangle is:", (0.5*b*h))
except Exception as e:
    print(e)
#Q4
try:
    x = int(input("enter 1st No: "))
    y = int(input("enter 2nd No: "))
    x,y = y,x
    print("1st no is ",x)
    print("2nd no is ",y)
except Exception as e:
    print(e)
#Q5 : Program to generate a random number
import random

print(random.randint(0,100))


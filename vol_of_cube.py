# import math
# radius1=(input("Enter the radius: "))
# radius2=float(radius1)
# vol= 4/3*math.pi*radius2**3
# print("The volume of circle with radius "+radius1+" is "+str(vol))


#Write a Python program to calculate the difference between a 
#given number and 17. If the number is greater than 17, return twice the absolute difference.

# number=int(input("Enter the number: "))
# if number>17:
#     print((2*(number-17)))
# else:
#     print(abs(17-number))    

# Write a Python program to test whether a number is within 100 of 1000 or 2000.
# number=int(input("Enter the number: "))
# def nearthousand(n):
#     return (abs(1000-n)<=100 or abs(2000-n)<=100)

# print(nearthousand(number))


#Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
# num1=int(input("Enter number 1: "))
# num2=int(input("Enter number 2: "))
# num3=int(input("Enter number 3: "))
# if num1==num2==num3:
#     print(3*(num1+num2+num3))
# else:
#     sum=num1+num2+num3
#     print(sum)

def sum(x,y,z):
    sum=x+y+z

    if x==y==z:
        sum *=3
    
    return sum
print(sum(5,5,5))
print(sum(5,6,5))
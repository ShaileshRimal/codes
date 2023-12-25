num=int(input("Enter the number: "))

def oddeven(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
    
print(f"The entered number is {oddeven(num)}")
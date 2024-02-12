# def addint(x,y):
#     if isinstance(x,int) and isinstance(y,int):
#         print(f"Sum= {x+y}")
#     else:
#         print("Enter the integer numbers!")
    
# print(addint(10,3))

def addint(x, y):
    if isinstance(x, int) and isinstance(y, int):
        print(f"Sum = {x + y}")
        return x + y  # Return the sum
    else:
        print("Enter integer numbers!")

# Call the function
result = addint(10.2, 3)
print("Result:", result)  # This will print "Result: 13"

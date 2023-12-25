#when split is done then it automatically put all the data into list
random=input("Enter the numbers seperated by comma: ")
random=random.split(",")
tuple=tuple(random)
print(tuple)
print(random)
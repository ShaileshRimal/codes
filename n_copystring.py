name=input("Enter the string: ")
num=int(input("Enter the number: "))


def cpystr(result,n):
    for i in range(1,n):
        result+=result
    return result
# for i in range(0,num):
#     print(cpystr(name))  #
#     i+=1
print(cpystr(name,num))
    
    
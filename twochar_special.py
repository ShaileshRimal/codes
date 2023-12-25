name=input("Enter the string: ")
numm=int(input("Enter the number: "))
n=len(name)


def cpy(text,num):
        result=""
        for i in range(0,num):
               result+=text
        return result

temp=name[:2]

if n<2:
      print(cpy(name,numm))
else:
      print(cpy(temp,numm))


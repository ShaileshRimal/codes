a=int(input("Enter an integer: "))
# # print(n+int(str(n)+str(n))+int(str(n)+str(n)+str(n)))
n1 = int("%i" %a)
n2 = int("%i%i" %(a, a))
n3 = int("%i%i%i" %(a, a, a))
print(n1+n2+n3)

#using f-string
# print(int(f"{a}")+int(f"{a}"f"{a}")+int(f"{a}"f"{a}"f"{a}"))

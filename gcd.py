

x=int(input("x= "))
y=int(input("y= "))
hcf=1

if x>y:
    min=y

else:
    min=x;

for i in range(1,min+1):
    if (x%i==0) and (y%i==0):
        hcf=i

print(f"gcd id {hcf}")



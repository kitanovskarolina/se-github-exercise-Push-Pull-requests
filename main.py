from swap import s
from extras.desc import d

a = int(input("Enter the first number (0-3): "))
b = int(input("Enter the second number (0-3): "))

aswaped,bswaped=s(a,b)
print(f'The numbers swaped are {aswaped}, and {bswaped}')

c=int(input("enter the value of c"))
cdesc=d(c)
print(f'c')

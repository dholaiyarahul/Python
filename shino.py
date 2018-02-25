from fractions import Fraction
num=input()
a,b=num.split()
num1=int(a)
num2=int(b)


#num1,num2=int(input('Enter Two numbers:')),int(input())

def gcd(num1,num2):
    if num2>num1:
        (num1,num2)=(num2,num1)
    if (num1%num2==0):
        return num2
    else:
        return gcd(num2,num1%num2)
max1=gcd(num1,num2)
ncf=0

for i in range(1,max1+1):
    print('Max1',max1)
    if(num1%i==0 and num2%i==0):
        ncf=ncf+1

print('\nNumber of common factor:', ncf)

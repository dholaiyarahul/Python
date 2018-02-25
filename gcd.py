num1,num2 = int(input('Enter Two Number:')),int(input())

def gcd(num1,num2):
    if num2>num1:
        (num1,num2)=(num2,num1)
    if (num1%num2==0):
        return num2
    else:
        return gcd(num2,num1-num2)

def gcd2(num1,num2):
    if num2>num1:
        (num1,num2)=(num2,num1)
    if (num1%num2==0):
        return num2
    else:
        return gcd2(num2,num1%num2)

def gcd1(num1,num2):
    fn1=[]
    fn2=[]
    cf=[]
    for i in range(1,num1+1):
        if (num1%i==0):
            fn1.append(i)
    for j in range(1,num2+1):
        if (num2%j==0):
            fn2.append(j)
    for i in fn1:
         if i in fn2:
            cf.append(i)
    return (cf[-1])

print('gcd:',gcd(num1,num2))
print('gcd1:',gcd1(num1,num2))
print('GCD2:',gcd2(num1,num2))

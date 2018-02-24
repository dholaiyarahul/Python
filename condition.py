mark=int(input('Enput ypur mark:'))
if (mark > 80):
    print('gread A')
elif (mark > 60) and (mark <= 80):
    print('grade B')
else:
    print('Grade C')



 #Loop
for i in range(20):
    if (i%2==0):
        print(i)


#function

def add(a,b):
    return a+b

num1=5
num2=3

print(add(num1,num2))
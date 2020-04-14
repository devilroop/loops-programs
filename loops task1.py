'''#program1
#check whether a no is prime or not
n=33
for i in range(2,n):
    if n%i==0:
        print(n,"is not primre number")
        break
else:
    print(n,"is primre number")
#program2
#check list of prime numbers within a range
a=int(input("starting number:"))
b=int(input("ending number:"))
for num in range(a,b):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)'''
#program5
#sum of digits and sum is evev or odd

a=input("first number:")
b=input("second number:")
total=0
for i in (a,b):
  total=total+int(i)
print(total)
if total%2==0:
    print("even")
else:
    print("odd")
         

'''# program no7                   
n=[2,3,4,5,6,7,10,4,10,3,5,6,7,7,8,9,1,2,3,4,5]
even=[]
odd=[]
for i in n:
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
print(even)
print(odd)
if sum(even)==sum(odd):
    print("even sum equal to odd sum")
else:
        print("even sum not equal to odd sum ")

##program8
#add all positive numbers, negative numbers in a number separately, check whether both are equal or not

n=[2,3,-4,5,6,-7,10,4,-10,3,-5,6,-7,7,8,-9,1,2,3,4,-5]
pve=[]
nve=[]
for i in n:
    if i>0:
        pve.append(i)
    elif i<0:
        nve.append(i)

if pve==nve:
    print("positive numbers sum equal to negitive sum")
else:
    print("positive numbers sum not equal to negitive")
#program11
#factorial of a number
num=6
f=1
for i in range(1,num+1):
    f=f*i
print(f)
# #program12
#fibonacci series   

num=10
a=0
b=1
if num==1:
    print(a)
else:
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c)'''

print("---------------ksp_task-6-------------------")
#reading integer input from user
z=input()

#reading integer input from user
a=int(input())

#operators
print("Arthmetical operators")
a=10
b=5
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)
print(a**b)
print(a%b)

print("Assignmental operators")

b+=1
print(b)
b-=2
print(b)
b*=4
print(b)
b/=2
print(b)
b%=3
print(b)
b**=3
print(b)

print("Relational operators")

print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)

print("Logical operators")
a=3
b=4
c=8
print(a<4 and c<=100)
print(a<=1 or b>c)
print(a!=3)

print("Identity operators")

print(a is b)
a=["red","blue"]
b=["red","blue"]
print(a is not b)
print("Membership Operators")
variable="good day"
print("day" in variable)
print("vysh" not in variable)


#Type casting
print("---Type casting---")
x=10
print(type(x))
print(float(x))
print(str(x))
e=True
print(e)

y=5.3
print(type(y))
print(int(y))
print(str(y))

#String Slicing

str1="this is a good day"
print(str1[1:7])
print(str1[:10])
print(str1[0:])
#conditional statements
age=int(input("enter the age"))
if(age<18):
    print("you are not eligible")
elif(age>18 and age<25):
    print("you are not eligible")
else:
    print("wrong input")
    
#LOOPS
print("For-Loop")
for i in range(5):
    print("hello")
    
print("while loop")
i=0
while(i<5):
    print("hello")
    
    







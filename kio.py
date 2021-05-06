a=int(input(" Enter the number"))
if a<0 :
    print("negative")
else:
    print("positive")
print("\n")
x=int(input("enter the first number"))
y=int(input("enter the second number"))
z=int(input(" enter the third number"))
if(x>y):
    if(x>z):
        print(x)
    else:
        print(z)
elif y>z:
    print(y)
else:
    print(z)
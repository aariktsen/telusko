n= int(input(" number   "))
j = n // 2
v=0
for i in range(1,j):
    if(n%i ==0):
        v =v +1
        pass
    else:
        print(end="")
if(v>1):
    print("even")
else:
    print("odd")













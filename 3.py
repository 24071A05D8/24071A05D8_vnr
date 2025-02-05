#gcd,lcm of 2 no.s
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=max(x,y)
while(z<=x*y):
    if(z%x==0 and z%y==0):
        break
    z+=1
print(str(z)+" is lcm of "+str(x)+" "+str(y))
i=min(x,y)
flag=0
while(z>=1):
    if(x%i==0 and y%i==0):
        break
    i-=1

print(str(i)+" is gcd")

    

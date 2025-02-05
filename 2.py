
def fibonacci(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)
x=int(input("Enter number of terms: "))
for i in range(1,x+1):
    print(fibonacci(i))


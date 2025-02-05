def add(n,m):
    print(n+m)
def sub(n,m):
    print(n-m)
def mult(n,m):
    print(n*m)
def div(n,m):
    if(m==0):
        print("division by 0 not possible")
    else:
        print(n/m)
def calculator():
    print("Enter")
    print("1:Addition")
    print("2:Substraction")
    print("3:Multiplication")
    print("4:Division")
    x=int(input( ))
    n=float(input("Enter a number: "))
    m=float(input("Enter a number: "))
    if(x==1):
        add(n,m)
    elif(x==2):
        sub(n,m)
    elif(x==3):
        mult(n,m)
    elif(x==4):
        div(n,m)
    else:
        print("enter a valid option(1-4)")
calculator()
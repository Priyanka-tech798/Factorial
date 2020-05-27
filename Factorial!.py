#Factorial of a given number by using Recursive
def fact(n):
    return 1 if (n==0 or n==1) else n*fact(n-1)
num = 5
print("Factorial of ",num,"is",fact(num))


#Factorial of a number by using iterative
def fact(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        f=1
        while n>1:
            f*=n
            n-=1
        return f    
            
num = 5
print("Factorial of ",num,"is",fact(num))


num = int(input("enter any number "))
def fibonacciNumbers(n):
    a=0
    b=1
    if(n<1):
        return
    print(a, end='')
    for x in range(1,n):
        print(b, end='')
        sum =a+b
        a=b
        b=sum
print(fibonacciNumbers(num), sep="")
def fib(n):
    if n  < 0:
        print("INCORRECT INPUT")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

num = 10
if num <= 0:
    print("enter a positive value")
else:
    print("fiboannchi sequece is equal to ")
    for i in range(num):
        print(fib(i))





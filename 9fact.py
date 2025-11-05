while 1:
    num=int(input("enter the number:"))
    def factorial(n):
        if n==0 or n==1:
            return 1
        else:
            return n * (factorial(n-1))
    print("The factorial is:  ",factorial(num))

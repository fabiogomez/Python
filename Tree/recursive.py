def summation(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + summation(n - 1)

def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def exponentation(n: int, p: int) -> int:
    if p == 1:
        return n
    else:
        return n*exponentation(n,p-1) 



if __name__ == "__main__":
    n = int(input("Give me a number: "))
    print("factorial is: "+str(summation(n)))
    print("factorial is:"+str(factorial(n)))
    print(exponentation(5,3))
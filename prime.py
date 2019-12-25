import time
import math


def prime(n):
    start = time.time()
    for num in range(2, int(math.sqrt(n+1))):
        x = 0
        while x < n:
            for i in range(2, n+1):
                x = num * i
                if x == n:
                    stop = time.time()
                    print(n, "is divisible by", num, "and", i)
                    print(n, "is not prime")
                    print("time taken is", stop-start)
                    exit()
    stop = time.time()
    print("time taken is", stop - start)
    print(n, "is prime")


y = int(input("Enter value of n"))
prime(y)

""" N is an integer. We are interested in finding if N is a special number. A special number is defined as a number
that can be represented as i power i , i  being an integer. A number should return Yes even if it can be converted
to a special number by subtracting square of one of the digits(one or more times).
example
input 1: 27
output : yes // 3**3 = 27
input 2: 31
output : yes // 36 - --> 36 - 9 = 27 (3**3 = 27)
input 3: 23
output : no  //23 - multiples of 4 = 19,15,11,7,3
             //23 - multiples of 9 = 14,5
             none of these can be represented as i**i
"""


def main():
    n = 31
    spl_numbers = []
    options = []
    for i in range(1,10):
        temp = i**i
        if temp > n:
            break
        spl_numbers.append(temp)
    if n in spl_numbers:
        print("YES")
        exit()
    else:
        for y in str(n):
            options.append(int(y)**2)
        for snum in spl_numbers:
            for num in options:
                x = (n-snum)
                if (x in spl_numbers) or (x % num == 0):
                    print("YES")
                    exit()
    print("NO")


main()

# Problem: There are n stairs, a person standing at the bottom wants to reach the top.
# The person can climb either 1 stair or 2 stairs at a time.
# Count the number of ways, the person can reach the top.
# Use dynamic programing
number_of_ways_memo = {}


def number_of_ways_memoized(n):
    if n in number_of_ways_memo:
        return number_of_ways_memo[n]
    elif n == 1:
        value = 1
    elif n == 2:
        value = 2
    else:
        value = number_of_ways_memoized(n - 1) + number_of_ways_memoized(n - 2)
    number_of_ways_memo[n] = value
    return value


n = int(input("Enter the number of stairs"))
for y in range(1, n+1):
    print(y, ":", number_of_ways_memoized(y))

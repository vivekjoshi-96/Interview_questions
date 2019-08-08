# Problem: There are n stairs, a person standing at the bottom wants to reach the top.
# The person can climb either 1 stair or 2 stairs at a time.
# Count the number of ways, the person can reach the top.


def number_of_ways(n):
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    else:
        value = number_of_ways(n - 1) + number_of_ways(n - 2)
    return value


n = int(input("Enter the number of stairs"))
for y in range(1, n+1):
    print(y, ":", number_of_ways(y))

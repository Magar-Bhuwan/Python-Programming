n = int(input("Enter a number: "))

for i in range(1, n+1):
    spaces = 2 * (n-1)
    stars = 2 * i - 1
    print("" * spaces + "*" * stars)

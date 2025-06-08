#Code to display a pyramid using '*'
def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

n = int(input("Enter number of Rows: "))
pyramid(n)

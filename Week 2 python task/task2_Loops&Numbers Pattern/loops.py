n = int(input("Enter a positive number: "))

if n <= 0:
    print("Please enter a positive number.")

else:
    # Print numbers from 1 to N using a for loop
    print("\nNumbers from 1 to", n, ":")

    for i in range(1, n + 1):
        print(i)

    # Print numbers from N to 1 using a while loop
    print("\nNumbers from", n, "to 1:")

    i = n

    while i >= 1:
        print(i)
        i -= 1

    # Print the multiplication table
    print("\nMultiplication table of", n, ":")

    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
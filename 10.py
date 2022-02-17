row = int(input("Input: "))

for i in range( 1, row + 1 ):
    for j in range ( (row + 1) - i ):
        print(" ", end = "")
    for k in range( 2 * i - 1 ):
        print("*", end = "")
    print()
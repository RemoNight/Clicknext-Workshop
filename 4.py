row = int(input("Input: "))

for i in range( 1, row + 1 ):
    for j in range ( i ):
        print(" ", end = "")
    for k in range( 0, 2 * (row - i) + 1 ):
        print("*", end = "")
    print()
k = 1
row = int(input("Input: "))

if row > 4:
    print("You can only input a maximum value of 4!")
else:
    for i in range( 1, row + 1 ):
        for j in range ( (row + 1) - i ):
            print(" ", end = "")
        for n in range( 1, i + 1 ):
            print(k, end = " ")
            if k == 9:
                k = 0
            else:
                k += 1

        print()
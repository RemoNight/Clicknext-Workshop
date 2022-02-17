def words(str1_low, str2_low):
    
    if len(str1_low) == len(str2_low):

        for i in str1_low:
            lst.append(i)

        for i in str2_low:
            lst2.append(i)

        for i in range(len(lst) - 1):
            for j in range(i+1,len(lst)):
                if lst[i] > lst[j]:
                    temp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = temp

        for i in range(len(lst2) - 1):
            for j in range(i+1,len(lst2)):
                if lst2[i] > lst2[j]:
                    temp = lst2[i]
                    lst2[i] = lst2[j]
                    lst2[j] = temp

        if lst == lst2:
            print("True")
        else:
            print("False")
    else:
        print("False")

lst = []
lst2 = []
str1 = input("Word 1: ")
str2 = input("Word 2: ")
str1_low = str1.lower()
str2_low = str2.lower()
words(str1_low, str2_low)









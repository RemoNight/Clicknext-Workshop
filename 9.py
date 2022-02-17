x = input("Enter your words: ")
n = ""
m = ""
lst = []
lst2 = []

for i in x:
    if i != " ":
        n += i
    if i == " ":
        lst.append(n)
        n = ""
lst.append(n)

for j in lst:
    for k in range(len(j) - 1,-1,-1):
        m += j[k]
    lst2.append(m)
    m = ""

for l in lst2:
    print(l, end=" ")
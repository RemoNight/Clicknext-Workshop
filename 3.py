# Example input 1, 2, 3, 4, 5
x = input("Input Array: ")
lst = []
n = ""

for i in x:
  if i != "," and i != " ":
    n += i
  if i == ",":
    lst.append(n)
    n = ""
lst.append(n)

for j in range(len(lst)):
  lst[j] = int(lst[j])
print('Array =', lst)

lst2 = []
i = 0

while i < len(lst) - 1:
    if lst[i + 1] - lst[i] != 1:
        lst2.append(lst[i])
    else:
        j = i
        a = i
        while j < len(lst) - 1:
            if lst[j + 1] - lst[j] == 1:
                j += 1
                i += 1
            else:
                break
        n = str(lst[a]) + "-" + str(lst[j])
        lst2.append(n)
    i += 1

if i < len(lst):
    lst2.append(lst[i]) # last number

print("Result: ")        
for i in lst2:
    y = len(lst2) - 1
    if i != lst2[y]:
        print(i, end=", ")
    else:
        print(i)


n = ""
temp = 0
lst = []
x = input("Input: ")

# split and add list
for i in x:
  if i != "," and i != " ":
    n += i
  if i == ",":
    lst.append(n)
    n = ""
lst.append(n)


for j in range(len(lst)):
  lst[j] = int(lst[j])


for k in range(len(lst)):
  for l in range(k):
    if lst[k] < lst[l]:
      temp = lst[k]
      lst[k] = lst[l]
      lst[l] = temp

for m in lst:
    y = len(lst) - 1
    if m == lst[y]: 
        print(str(m))
    else:
        print(str(m) + ",", end = " ")



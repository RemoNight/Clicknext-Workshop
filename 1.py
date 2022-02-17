lst = []
n = ""
m = ""

# Example input 1, 2, 3, 4, 5
x = input("Input Array: ")

for i in x:
  if i != "," and i != " ":
    n += i
  if i == ",":
    lst.append(n)
    n = ""
lst.append(n)


for j in range(len(lst)):
  lst[j] = int(lst[j])


sum = int(input("Sum: "))
print("\nArray =", lst)

for j in range(len(lst)):
    for k in range(j):
        if lst[j] + lst[k] == sum:
            if lst[j] > lst[k]:
                m +=  str(lst[j]) + "," + str(lst[k]) + "\n"

print("Result:", m[-1::-1])
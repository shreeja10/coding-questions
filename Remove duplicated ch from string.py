s = input("enter a string as input: ")

s_set = set()
new = ""

for i in s:
    if i not in s_set:
        s_set.add(i)
        new += i

print(new)
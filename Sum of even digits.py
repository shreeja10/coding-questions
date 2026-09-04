num=int(input("Enter a number:  "))
num_str=str(num)
total=0
for i in num_str:
    if int(i)%2==0:
        total+=int(i)
print(total)
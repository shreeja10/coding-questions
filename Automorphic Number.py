num=int(input("Enter a number:  "))
square = num*num
last=0
x=10**len(str(num))
last=square%x
if last==num:
    print("automorphic number")
else:
    print("not automorphic number")
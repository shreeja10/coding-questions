num=int(input("Enter a number:  "))
last=0
rev=0
original=num
while num>0:
    last=num%10
    rev=rev*10+last
    num=num//10
print(abs(original-rev))
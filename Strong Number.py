num=145
last=0
original=num
sum=0
while num>0:
    product=1
    last=num%10
    for i in range(1,last+1):
        product*=i
    sum+=product
    num=num//10
if original==sum:
    print("strong")
else:
    print("not strong")
nums = [5, 2, 8, 2, 3, 5, 1]
new=[]
d={}
for i in nums:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in nums:
    if d[i]>1:
        new.append(i)
smallest=new[0]
for i in new:
    if i<smallest:
        smallest=i
print(smallest)
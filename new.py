nums=[1,3,5,5,-2,5,1,2,3,5]
d={}
for i in nums:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
largest=0
for keys,values in d.items():
    if values>largest:
        largest=keys
print(largest)
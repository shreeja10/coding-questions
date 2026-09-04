nums = [4, 1, 2, 1, 3, 4]
new={}
a=[]
for i in nums:
    if i not in new:
        new[i]=1
    else:
        new[i]+=1
for i in nums:
    if new[i]>1:
        a.append(i)
        a_set=set(a)
print(a_set)
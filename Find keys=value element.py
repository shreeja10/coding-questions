nums = [2, 3, 2, 4, 4, 4, 5]
d={}
ans=0
for i in nums:
  if i not in d:
    d[i]=1
  else:
    d[i]+=1
for i in nums:
  if i==d[i]:
    ans=i
print(ans)
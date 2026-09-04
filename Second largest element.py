nums = [10, 5, 8, 10, 3, 8]
largest=nums[0]
second_largest=float('-inf')
for i in nums:
    if i>largest:
        largest=i
for i in nums:
    if i!=largest and i>second_largest:
        second_largest=i
print(second_largest)
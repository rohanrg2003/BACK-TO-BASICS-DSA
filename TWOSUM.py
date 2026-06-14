nums=[1,2,3,4,5,14,15,18,23]
target=17
n=len(nums)
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            print([i,j])
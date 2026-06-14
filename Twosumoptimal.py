nums=[1,2,3,4,5,14,15,18,23]
target=17
hashmap={}
for i in range (0,len(nums)):
    remaining =target-nums[i]
    if remaining in hashmap:
        print([hashmap[remaining],i])
    hashmap[nums[i]]=i

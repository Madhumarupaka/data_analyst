# # sum of n natural numbers
# n = int(input())
# total=0
# for i in range(1,n+1):
#     total+=i
# print(total)
num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
# Write your code here
class Solution:
    def twoSum(self, nums, target):
        dict1={}
        for i in range(len(nums)):
            if target-nums[i] in dict1:
                return [dict1[target-nums[i]],i]
            dict1[nums[i]]=i
        return []
nums=[int(x) for x in input().split(",")]
target=int(input())
s=Solution()
print(s.twoSum(nums,target))


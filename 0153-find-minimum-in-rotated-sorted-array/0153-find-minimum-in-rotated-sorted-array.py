# brute force solution 
class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        mini=float('inf')
        for i in range(n):
            if nums[i]<mini:
                mini=nums[i]
        return mini


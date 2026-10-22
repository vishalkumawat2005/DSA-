class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        maxx=float('-inf')
        n=len(nums)
        index=0
        for i in range(0,n):
            if nums[i]>maxx:
                maxx=nums[i]
                index=i
        return index
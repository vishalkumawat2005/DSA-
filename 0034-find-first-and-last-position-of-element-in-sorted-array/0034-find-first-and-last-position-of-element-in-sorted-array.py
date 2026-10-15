class Solution:
    def lowerbound(self,num,target):
        n=len(num)
        lb=-1
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if num[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    def upperbound(self,nums,target):
        ub=-1
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = self.lowerbound(nums, target)
        if lb == -1 or nums[lb] != target:
            return [-1, -1]
        ub = self.upperbound(nums, target)
        if ub == -1:
            return [lb, len(nums) - 1]
        return [lb, ub - 1]
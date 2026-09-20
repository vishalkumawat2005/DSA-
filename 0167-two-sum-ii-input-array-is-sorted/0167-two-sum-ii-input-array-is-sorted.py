class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0
        nums=numbers
        right=len(nums)-1
        while left<right:
            sum1=nums[left]+nums[right]
            if sum1==target:
                return[left+1,right+1]
            elif sum1>target:
                right-=1
            else:
                left+=1
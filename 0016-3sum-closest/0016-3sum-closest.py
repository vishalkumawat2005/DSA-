class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        cs=float('-inf')
        nums.sort()
        for i in range(len(nums)-1):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                ts=nums[i]+nums[l]+nums[r]
                if (abs(cs-target)>abs(ts-target)):
                    cs=ts
                elif ts>target:
                    r-=1
                elif ts<target:
                    l+=1
                else:
                    return ts
        return cs
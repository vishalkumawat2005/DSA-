class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        freq={}
        for i in range(0,n+1):
            freq[i]=0
        for i in nums:
            freq[i]=1
        for k,v in freq.items():
            if v==0:
                return k        
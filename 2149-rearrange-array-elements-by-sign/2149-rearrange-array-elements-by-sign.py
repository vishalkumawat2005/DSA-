class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        neg=[]
        pos=[]
        res=[]
        for i in range(0,len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        for j in range(0,len(pos)):
            res.append(pos[j])
            res.append(neg[j])
        return res
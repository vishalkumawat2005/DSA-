class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        j=0
        for k in freq:
            nums[j]=k
            j+=1
        return j
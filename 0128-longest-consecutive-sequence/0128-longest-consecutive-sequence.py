class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # n=len(nums)
        # max_count=0
        # for i in range(0,len(nums)):
        #     num=nums[i]
        #     count=1
        #     while num+1 in nums:
        #         count+=1
        #         num=num+1
        #     max_count=max(max_count,count)
        # return max_count
        longest=0
        s=set(nums)
        for x in s:
            i=1
            if x-i not in s:
                while x+i in s:
                    i+=1
                longest=max(longest,i)
        return longest
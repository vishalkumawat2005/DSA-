class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp=[]
        for i in range(0,n):
            if nums[i]!=0:
                temp.append(nums[i])
        nl=len(temp)
        for j in range(0,nl):
            nums[j]=temp[j]
        for k in range(nl,n):
            nums[k]=0

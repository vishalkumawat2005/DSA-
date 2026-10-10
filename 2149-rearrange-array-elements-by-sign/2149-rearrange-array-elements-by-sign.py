class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        # n=len(nums)
        # neg=[]
        # pos=[]
        # res=[]
        # for i in range(0,len(nums)):
        #     if nums[i]>0:
        #         pos.append(nums[i])
        #     else:
        #         neg.append(nums[i])
        # for j in range(0,len(pos)):
        #     res.append(pos[j])
        #     res.append(neg[j])
        # return res

        # n=len(nums)
        # neg=[]
        # pos=[]
        # for i in range(0,len(nums)):
        #     if nums[i]>0:
        #         pos.append(nums[i])
        #     else:
        #         neg.append(nums[i])
        # for i in range(0,len(pos)):
        #     nums[i*2]=pos[i]
        #     nums[(i*2)+1]=neg[i]
        # return nums



        #optimal solution
        n=len(nums)
        res=[0]*n
        pos_ind,neg_ind=0,1
        for i in range(0,n):
            if nums[i]>=0:
                res[pos_ind]=nums[i]
                pos_ind+=2
            else:
                res[neg_ind]=nums[i]
                neg_ind+=2
        return res
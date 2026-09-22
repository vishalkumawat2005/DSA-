class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res_set=set()
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                hash_set=set()
                for k in range(j+1,n):
                    fourth=target-(nums[i]+nums[j]+nums[k])
                    if fourth in hash_set:
                        total=[nums[i],nums[j],nums[k],fourth]
                        total.sort()
                        res_set.add(tuple(total))
                    hash_set.add(nums[k])
        return [list(ans) for ans in res_set]
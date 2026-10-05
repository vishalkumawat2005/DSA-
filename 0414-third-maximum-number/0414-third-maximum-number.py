class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        n = len(nums)

        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')

        for i in range(n):
            if nums[i] > max1:
                max1 = nums[i]

        for i in range(n):
            if nums[i] > max2 and nums[i] != max1:
                max2 = nums[i]

        for i in range(n):
            if nums[i] > max3 and nums[i] != max1 and nums[i] != max2:
                max3 = nums[i]

        if max3 == float('-inf'):
            return max1

        return max3
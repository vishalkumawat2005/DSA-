class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first=second=third=float('-inf')
        for n in set(nums):
            if n>first:
                first,second,third=n,first,second
            elif n>second:
                second ,third=n,second
            elif n>third:
                third=n
        return third if third!=float('-inf') else first
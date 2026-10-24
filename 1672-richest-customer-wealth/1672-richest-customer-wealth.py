class Solution:
    def maximumWealth(self, acc: list[list[int]]) -> int:
        max_ans=0
        for i in range(0,len(acc)):
            ans=0
            for j in range(0,len(acc[0])):
                ans+=acc[i][j]
            if ans>max_ans:
                max_ans=ans
        return max_ans


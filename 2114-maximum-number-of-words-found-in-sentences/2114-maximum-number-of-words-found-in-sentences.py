class Solution:
    def mostWordsFound(self, sen: list[str]) -> int:
        ans=0
        count=0
        for i in sen:
            count=len(i.split())
            ans=max(ans,count)
        return ans
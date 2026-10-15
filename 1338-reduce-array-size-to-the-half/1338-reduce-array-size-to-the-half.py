class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
        counts=sorted(freq.values(),reverse=True)
        rem=0
        ans=0
        n=len(arr)
        for count in counts:
            rem+=count
            ans+=1
            if rem>= n//2:
                return ans
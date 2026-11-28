class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        n=len(hours)
        count=0
        for i in range(0,n):
            if hours[i]>=target:
                count+=1
        return count
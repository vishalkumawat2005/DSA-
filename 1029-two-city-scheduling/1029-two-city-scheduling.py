class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key=lambda x:x[1]-x[0])
        total=0
        n=len(costs)//2
        for i in range(len(costs)):
            if i<n:
                total+=costs[i][1]
            else:
                total+=costs[i][0]
        return total
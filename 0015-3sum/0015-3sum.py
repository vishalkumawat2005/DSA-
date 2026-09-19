#brute force solution

# class Solution:
#     def threeSum(self, arr: list[int]) -> list[list[int]]:
#         my_set=set()
#         n=len(arr)
#         for i in range(n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     if arr[i]+arr[j]+arr[k]==0:
#                         temp=[arr[i],arr[j],arr[k]]
#                         temp.sort()
#                         my_set.add(tuple(temp))
#         return [ list(ans) for ans in my_set]
class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        res=set()
        for i in range(0,len(arr)):
            my_set=set()
            for j in range(i+1,len(arr)):
                third=-(arr[i]+arr[j])
                if third in my_set:
                    temp=[arr[i],arr[j],third]
                    temp.sort()
                    res.add(tuple(temp))
                my_set.add(arr[j])
        return [list(ans) for ans in res] 
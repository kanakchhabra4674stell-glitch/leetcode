class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        ans=[]
        for i in range(len(l)):
            arr=nums[l[i]:r[i]+1]
            arr.sort()
            diff=arr[1]-arr[0]
            is_arith=True
            for j in range(1,len(arr)-1):
                if arr[j+1]-arr[j]!=diff:
                    is_arith=False
                    break
            ans.append(is_arith)
        return ans
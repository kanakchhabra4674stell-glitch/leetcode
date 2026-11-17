class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total=sum(nums)
        left,ans=0,0
        for i in range(len(nums)-1):
            left+=nums[i]
            right=total-left
            if(left-right)%2==0: ans+=1
        return ans
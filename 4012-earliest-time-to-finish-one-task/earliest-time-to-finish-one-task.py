class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans=float("inf")
        for start,time in tasks:
            finish=start+time
            ans=min(ans,finish)
        return ans
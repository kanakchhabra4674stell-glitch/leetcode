class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n=len(prices)
        dp=[[[-1]*2 for _ in range(k+1)]for _ in range(n+1)]
        def f(i,k,hold):
            # bc
            if k==0: return 0 
            if i==n: return 0
            if dp[i][k][hold]!=-1: return dp[i][k][hold]
            # exclude
            ans=f(i+1,k,hold)
            # include
            if hold==0: ans=max(ans,-prices[i]+f(i+1,k,1))
            else: ans=max(ans,prices[i]+f(i+1,k-1,0))
            dp[i][k][hold]=ans
            return dp[i][k][hold]
        return f(0,k,0)
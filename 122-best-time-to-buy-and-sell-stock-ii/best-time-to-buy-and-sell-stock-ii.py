class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp=[[-1 for _ in range(n)]for _ in range(2)]
        def f(i,hold):
            if i==n: return 0
            if dp[hold][i]!=-1: return dp[hold][i]
            if hold==0:
                buy=-1*(prices[i])+f(i+1,1)
                skip=f(i+1,0)
                profit=max(buy,skip)
            else:
                sell=prices[i]+f(i+1,0)
                skip=f(i+1,1)
                profit=max(sell,skip)
            dp[hold][i]=profit
            return profit
        return f(0,0)
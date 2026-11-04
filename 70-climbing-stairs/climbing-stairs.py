class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def f(i):
            if i==0: return 1
            if i<0: return 0 
            if dp[i]!=-1: return  dp[i]
            one=f(i-1)
            two=f(i-2)
            dp[i]=one+two
            return dp[i]
        return f(n)
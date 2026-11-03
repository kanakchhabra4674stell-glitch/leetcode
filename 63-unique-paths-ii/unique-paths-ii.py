class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1 for _ in range(n)]for i in range(m)]
        def f(i,j):
            if i>=m or j>=n: return 0
            if obstacleGrid[i][j]==1: return 0
            if i==m-1 and j==n-1: return 1
            if dp[i][j]!=-1: return dp[i][j]
            ways=0
            if obstacleGrid[i][j]==0: ways=f(i+1,j)+f(i,j+1) 
            dp[i][j]=ways
            return dp[i][j]
        return f(0,0)
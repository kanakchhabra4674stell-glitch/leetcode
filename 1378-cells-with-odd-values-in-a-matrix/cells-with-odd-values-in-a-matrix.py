class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows,cols=[0]*m,[0]*n
        for r,c in indices:
            rows[r]+=1
            cols[c]+=1
        ans=0
        for i in range(m):
            for j in range(n):
                if(rows[i]+cols[j])%2!=0: ans+=1
        return ans
class Solution:
    def countDigits(self, num: int) -> int:
        temp,ans=num,0
        while temp>0:
            digit=temp%10
            if num%digit==0: ans+=1
            temp//=10
        return ans
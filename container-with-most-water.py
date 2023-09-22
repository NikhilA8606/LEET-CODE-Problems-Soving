class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        res = 0
        for i,x in enumerate(height):
            for j in range(i+1,l):
                v = (j-i) * min(x,height[j])
                res = max(res,v)
        return res



        
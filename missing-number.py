class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lis = [i for i in range(len(nums)+1)]
        d = list(set(lis) - set(nums))
        return d[0]
        
        

        
        
        

        
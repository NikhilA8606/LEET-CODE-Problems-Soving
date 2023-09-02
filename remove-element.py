class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        while val in nums:
            nums.remove(val)
        self.k = len(nums)
        return self.k
        
        
            

        

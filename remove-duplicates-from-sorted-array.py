class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lis = list(set(nums))
        nums.clear()
        for i in range(len(lis)):
            nums.append(lis[i])
        nums.sort()      
        return len(lis)
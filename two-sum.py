class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    self.lis = []
                    self.lis.append(i)
                    self.lis.append(j)
                    break
        return self.lis

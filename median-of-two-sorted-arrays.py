import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lis = nums1 + nums2
        lis.sort()
        n = len(lis)
        if n%2 != 0:
            return lis[n//2]
        else: 
            i = lis[n//2 -1] + lis[n//2]
            return (i/2)

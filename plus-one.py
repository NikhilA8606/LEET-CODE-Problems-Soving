class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = ""
        for i in digits:
            r += str(i)
        val = int(r) + 1
        lis = [int(i) for i in str(val)]
        return lis
        
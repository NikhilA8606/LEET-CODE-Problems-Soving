import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = s.split()
        l  = li[-1]
        return len(l)
        
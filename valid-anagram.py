from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        c1 = Counter(a)
        c2 = Counter(b)
        return True if c1 == c2 else False



        
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if st == st[::-1]:
            return True
        else:
            return False
        
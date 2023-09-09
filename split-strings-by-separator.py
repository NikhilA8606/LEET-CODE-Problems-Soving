class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for i in words:
            li = i.split(separator)
            res += li
        resu = [i for i in res if i]
        return resu
        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if digits == "":
            return []
        num = list(dic[digits[0]])
        for i in digits[1:]:
            num = [a+b for a in num for b in list(dic[i])]
        return num
                
            

       
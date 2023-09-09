class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            print("false")
        else:
            self.lis = list(x)
            self.flag = 0
            for i in range(len(lis)//2):
                if lis[i] != lis[len(lis)-i+1]:
                    self.flag = 1
                    break
            if flag == 0:
                print("true")
            else:
                print("false")
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        if(x <= 9):
            return True

        counter = 1
        while x >= 10 * counter:
            counter *= 10

        while counter != 0:
            r = x % 10
            if(x // counter != r):
                return False
            x = (x % counter) // 10
            counter = counter // 100

        return True

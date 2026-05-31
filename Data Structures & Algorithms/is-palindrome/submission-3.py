class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if(s[l].isalnum() == False):
                l += 1
            elif(s[r].isalnum() == False):
                r -= 1
            else:
                if(s[l].lower() != s[r].lower()):
                    return False
                else:
                    r -= 1
                    l += 1
        return True

            

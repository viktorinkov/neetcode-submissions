class Solution:
    def isPalindrome(self, s: str) -> bool:
        origin = []
        for char in s:
            if(char.isalnum()):
                origin.append(char)
        
        # go reverse
        rev = list(reversed(origin))
        n = len(origin)
        for i in range(n):
            if(origin[i].lower() != rev[i].lower()):
                return False
        return True
class Solution:
    def isValid(self, s: str) -> bool:
        group = {'(' :')', '{':'}', '[': ']'}

        stack = []
        for char in s:
            if(char in group):
                stack.append(group[char])
            else:
                if(len(stack) == 0):
                    return False
                if(stack[-1] == char):
                    stack.pop()                           
                else:
                    return False

        return len(stack) == 0

        


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        opened = ['(', '{', '[']
        pairs = {'(' :')', '{' : '}', '[' :']'}
        stack = []
        for char in s:
            if(char in opened):
                stack.append(pairs[char])
            else:
                if(len(stack) == 0 or char != stack.pop()):
                    return False
        
        return len(stack) == 0
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        myMap = {}
        start = ord('a') - 2
        for i in range(2, 10):
            r = 3
            if(i == 7 or i == 9):
                r = 4
            for j in range(r):
                if i not in myMap:
                    myMap[i] = []
                myMap[i].append(chr(start + i + j))
            start += r - 1
        print(myMap)
        def backT(i, cur):
            if i == len(digits):
                res.append(cur)
                return
            for c in myMap[int(digits[i])]:
                backT(i+1, cur + c)
            
        if digits:
            backT(0, "")
        return res
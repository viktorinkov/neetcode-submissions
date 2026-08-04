class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # naive
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1):
            for j in range(i+1, len(temperatures)):
                if(temperatures[j] > temperatures[i]):
                    res[i] = j - i
                    break
                else:
                    res[i] = 0

        return res
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we are counting until speed matches
        stack = []
        # we increase the stack until we find a slower car
        # then we pop the stack 
        
        orderedPairs = [()] * len(position)

        for i in range(len(position)):
            timeToDest = (target-position[i]) / speed[i]
            orderedPairs[i] = (position[i], timeToDest)

        orderedPairs = sorted(orderedPairs, key=lambda x: x[0])

        # _   _ _ _           10
        # 1   3 2 1

        for i in range(len(orderedPairs)-1, -1, -1):
            if(stack == [] or orderedPairs[i][1] > stack[-1][1]):
                stack.append(orderedPairs[i])

        return len(stack)
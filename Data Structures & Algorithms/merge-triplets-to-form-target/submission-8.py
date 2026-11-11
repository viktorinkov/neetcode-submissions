class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            valid.append(t)

        results = set()
        for t in valid:
            # just max them all
            for i in range(3):
                if t[i] == target[i]:
                    results.add(i)

        return len(results) == len(target)
            
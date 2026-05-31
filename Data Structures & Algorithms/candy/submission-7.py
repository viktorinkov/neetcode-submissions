class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arr = [1] * n
        
        # Left-to-right: check if right neighbor is bigger
        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                arr[i + 1] = arr[i] + 1
        
        # Right-to-left remains the same
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)
        
        return sum(arr)

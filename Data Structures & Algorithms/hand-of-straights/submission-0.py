class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freqs = Counter(hand)
        hand.sort()

        for num in hand:
            if freqs[num] > 0:
                for i in range(num, num + groupSize):
                    if not freqs[i]:
                        return False
                    freqs[i] -= 1
        
        return True

        
import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        heapq.heapify(self.maxHeap) ## use this for lower half of elememnts
        heapq.heapify(self.minHeap) ## use this for greater half of elements
        self.maxCount = 0
        self.minCount = 0

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
            
        if(self.maxCount > 0 and num < -self.maxHeap[0]):
            heapq.heappush(self.maxHeap, -(heapq.heappop(self.minHeap)))
            self.maxCount += 1
        else:
            self.minCount += 1
        ## rebalance
        if(abs(self.maxCount - self.minCount) > 1):
            if(self.maxCount > self.minCount):
                heapq.heappush(self.minHeap, -(heapq.heappop(self.maxHeap)))
                self.minCount += 1
                self.maxCount -= 1
            else:
                heapq.heappush(self.maxHeap, -(heapq.heappop(self.minHeap)))
                self.maxCount += 1
                self.minCount -= 1

    def findMedian(self) -> float:
        print(self.maxHeap)
        print(self.minHeap)
        if(self.maxCount == self.minCount):
            res = (self.minHeap[0] - self.maxHeap[0])/2.0
            return res
        elif(self.maxCount > self.minCount):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]
        
        
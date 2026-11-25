import heapq

class MedianFinder:

    def __init__(self):
        # small: max heap (smaller half)
        # large: min heap (larger half)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Decide which heap to insert into
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # Store negative values to simulate a max heap
            heapq.heappush(self.small, -num)

        # Rebalance if small has more than one extra element
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Rebalance if large has more than one extra element
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # Odd total: Return the root of the larger heap
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]

        # Even total: Return the average of both roots
        return (-self.small[0] + self.large[0]) / 2.0

# Mental Cue: Two heaps → Insert → Rebalance → Find median.
# RT: addNum O(log n) - Heap insertion and rebalancing.
# RT: findMedian O(1) - Direct access to heap roots.
# Space: O(n) - Store all elements across both heaps.
import heapq

class MedianFinder:

    def __init__(self):
        # small: max-heap (stores smaller half), large: min-heap (stores larger half)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # 1. Decide which heap to add to based on the current "middle"
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # Store as negative to simulate max-heap behavior
            heapq.heappush(self.small, -1 * num)
        
        # 2. Rebalance: Ensure size difference is no more than 1
        # Rebalancing involves a pop and a push, both are O(log n)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If odd total, median is the top of the larger heap: O(1)
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        # If even total, median is the average of both heap tops: O(1)
        return (-1 * self.small[0] + self.large[0]) / 2.0

# --- Complexity Analysis ---
# Time Complexity:
# - addNum(num): O(m*log n) -> log n for heap insertion/rebalancing.
# - findMedian(): O(m) -> Instant access to heap roots.
# Space Complexity:
# - O(n) -> To store all elements in the data stream.
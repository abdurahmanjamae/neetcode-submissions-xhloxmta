class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])

        res = [intervals[0]]

        for i in intervals[1:]:
            lastEnd = res[-1][1]
            if i[0] <= lastEnd:
                res[-1][1] = max(lastEnd,i[1])
            else:
                res.append(i)
        return res
        
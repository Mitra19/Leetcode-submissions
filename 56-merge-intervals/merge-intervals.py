class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        if len(intervals) == 1:
            return intervals
        for interval in intervals:
            if len(result) == 0 or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
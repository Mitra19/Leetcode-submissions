class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == n:
            return nums
        num_counter = Counter(nums)
        return heapq.nlargest(k, num_counter.keys(), key= num_counter.get)
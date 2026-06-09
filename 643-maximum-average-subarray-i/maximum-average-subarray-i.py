class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
        window_sum = sum(nums[:k])
        ans = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]
            ans = max(ans, window_sum)
        return ans / k

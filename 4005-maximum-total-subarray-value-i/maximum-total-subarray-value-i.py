class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        min_val = sorted_nums[0]
        max_val = sorted_nums[len(nums)-1]
        return (max_val-min_val)*k
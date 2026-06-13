class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1
        rightLen, leftLen = 0,0
        while(low<=high):
            mid = low + (high-low) // 2
            if (mid - 1 < 0 or nums[mid] != nums[mid-1]) and (mid + 1 == n or nums[mid] != nums[mid+1]):
                return nums[mid]
            leftLen = mid-1 if (nums[mid] == nums[mid-1]) else mid
            if leftLen % 2:
                high = mid - 1
            else:
                low = mid + 1
        
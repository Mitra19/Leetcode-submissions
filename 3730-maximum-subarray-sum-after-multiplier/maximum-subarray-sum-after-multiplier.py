class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        dp=[[0 for i in range(3)] for j in range(len(nums)+1)]
        dp1=[[0 for i in range(3)] for j in range(len(nums)+1)]
        max_val=float("-inf")
        for i in range(1,len(nums)+1):
            dp[i][0]=max(dp[i-1][0]+nums[i-1],nums[i-1])
            dp[i][1]=max(nums[i-1]*k,dp[i-1][0]+nums[i-1]*k,dp[i-1][1]+nums[i-1]*k)
            dp[i][2]=max(dp[i-1][1]+nums[i-1],dp[i-1][2]+nums[i-1])
            max_val=max(max_val,dp[i][0],dp[i][1],dp[i][2])
        for i in range(1,len(nums)+1):
            dp1[i][0]=max(dp1[i-1][0]+nums[i-1],nums[i-1])
            dp1[i][1]=max((floor(nums[i-1]/k) if nums[i-1]>=0 else ceil(nums[i-1]/k)),dp1[i-1][0]+(floor(nums[i-1]/k) if nums[i-1]>=0 else ceil(nums[i-1]/k)),dp1[i-1][1]+(floor(nums[i-1]/k) if nums[i-1]>=0 else ceil(nums[i-1]/k)))
            dp1[i][2]=max(dp1[i-1][1]+nums[i-1],dp1[i-1][2]+nums[i-1])
            max_val=max(max_val,dp1[i][0],dp1[i][1],dp1[i][2])
        return max_val    

        
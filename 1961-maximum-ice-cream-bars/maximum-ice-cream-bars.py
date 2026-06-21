class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = len(costs)
        if coins < costs[0]:
            return 0
        if coins >= sum(costs):
            return n
        ans = 0
        for i in range(n):
            if coins - costs[i] >= 0:
                ans += 1
                coins -= costs[i]
            else:
                break
        return ans

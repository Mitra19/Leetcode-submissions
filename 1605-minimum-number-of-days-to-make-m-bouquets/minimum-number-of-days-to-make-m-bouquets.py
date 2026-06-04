class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def canMake(days):
            bouquet = 0
            flower = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flower+=1
                else:
                    flower = 0
                if flower == k:
                    bouquet += 1
                    flower = 0
            return bouquet >= m
        lower = min(bloomDay)
        upper = max(bloomDay)
        ans = -1
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            if canMake(mid):
                ans = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return ans
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {"b": 0, "a": 0 ,"l": 0, "o":0, "n": 0}
        for ch in text:
            if ch in "balon":
                count[ch] += 1
        ans = float("inf")
        for key, value in count.items():
            print(f"key: {key}, value: {value}")
            if key in "ban":
                ans = min(ans, value)
            else:
                ans = min(ans , value//2)
        return ans
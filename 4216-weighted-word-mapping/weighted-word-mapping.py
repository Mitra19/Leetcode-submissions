class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for word in words:
            sum = 0
            for c in word:
                i = ord(c) - ord('a')
                sum+=weights[i]
            # print(sum)
            # print(sum%26)
            # print(26 - sum %26)
            sum = 26 - (sum % 26)
            ans += alpha[(sum % 26) - 1]
        return ans
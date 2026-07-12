class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_set = sorted(set(arr))
        index_dict = {}
        index = 1
        for i in arr_set:
            index_dict[i] = index
            index+=1
        ans = []
        for i in arr:
            ans.append(index_dict[i])
        return ans
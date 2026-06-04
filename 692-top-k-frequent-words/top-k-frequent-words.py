import heapq
class HeapItem:
    def __init__(self, word:str, count:str) -> None:
        self.word = word
        self.count = count
    def __lt__(self, compare_word:HeapItem) -> bool:
        if self.count == compare_word.count:
            return self.word > compare_word.word
        return self.count < compare_word.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counter = Counter(words)
        heap = []
        for key, count in word_counter.items():
            item = HeapItem(key, count)
            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                if item > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, item)
        ans = []
        while k:
            ans.append(heapq.heappop(heap).word)
            k-=1
        return ans[::-1]
        
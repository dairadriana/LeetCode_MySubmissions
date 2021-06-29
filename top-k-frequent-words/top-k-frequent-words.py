import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        my_words = {}
        for word in words:
            my_words[word] = words.count(word)
        heap = []
        heapq.heapify(heap)
        
        for key in my_words:
            heapq.heappush(heap, (-my_words[key], key))            
        res = []
        
        for i in range(k):
            popped = heapq.heappop(heap)
            res.append(popped[1])
        
        return res
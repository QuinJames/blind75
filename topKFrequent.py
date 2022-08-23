from collections import Counter
from heapq import *
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        max_heap = []
        for key, value in num_freq.items():
            heappush(max_heap, (-value, key))

        result = []
        for _ in range(k):
            result.append(heappop(max_heap)[1])
        return result


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))

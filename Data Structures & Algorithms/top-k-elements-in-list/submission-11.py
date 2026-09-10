from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        # Frequency of each number
        for i in nums:
            d[i] = d.get(i, 0) + 1

        # Sort numbers by frequency (highest first)
        sorted_items = sorted(d, key=d.get, reverse=True)

        # Return top k frequent elements
        return sorted_items[:k]

from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        d = Counter(nums)
        return [n[0] for n in d.most_common(k)]
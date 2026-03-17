from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequency
        count = Counter(nums)
        
        # Step 2: Create buckets
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, c in count.items():
            freq[c].append(num)
        
        # Step 3: Collect top k frequent
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
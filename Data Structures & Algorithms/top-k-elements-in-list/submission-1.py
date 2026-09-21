class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        buckets = [[] for i in range(len(nums))]

        for num in nums:
            count[num] += 1
        
        for key, val in count.items():
            buckets[val-1].append(key)
        
        topK = []
        idx = len(buckets)- 1
        while len(topK) < k:
            topK += buckets[idx]
            idx -= 1


        return topK[:k] 
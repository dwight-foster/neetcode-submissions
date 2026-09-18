class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        count = sorted(count.keys(), key=count.get, reverse=True)

        return count[:k] 
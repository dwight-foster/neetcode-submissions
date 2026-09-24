class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            mid = (l+r)//2
            time = 0
            print(l, r)
            for p in piles:
                time += math.ceil(float(p)/mid)
            print(time)
            if time <= h:
                r = mid - 1
                k = mid
            else:
                l = mid + 1
 
        return k
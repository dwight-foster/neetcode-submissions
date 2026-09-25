class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        highest_count = 0
        longest = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            highest_count = max(highest_count, count[s[r]])
            while (r - l + 1) - highest_count > k:
                count[s[l]] -= 1
                l += 1
            longest = max(r - l + 1, longest)
        return longest

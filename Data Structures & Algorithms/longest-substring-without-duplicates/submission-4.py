class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        l = 0
        longest = 0 
        for r in range(len(s)):
            if s[r] in counter:
                l = max(counter[s[r]]+1, l)

            counter[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest
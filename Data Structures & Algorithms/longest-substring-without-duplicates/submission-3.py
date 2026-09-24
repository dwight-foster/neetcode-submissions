class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        stack = []
        longest = 0 
        for char in s:

            if counter.get(char, 0) > 0:
                while stack and counter[char] > 0:
                    c = stack.pop(0)
                    counter[c] -= 1
            counter[char] = 1
            stack.append(char)
            longest = max(len(stack), longest) 
        return longest
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            print(s[i], s[j])
            if s[j].lower() != s[i].lower():
                return False

            else:
                i += 1
                j -= 1

        return True
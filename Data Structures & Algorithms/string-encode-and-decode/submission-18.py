class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for s in strs:
            out += f'{len(s)}/'
            out += s
        return out

    
    def decode(self, s: str) -> List[str]:
        out = []
        idx = 0
        while idx < len(s):
            j = idx
            print(idx)
            while s[j] != "/":
                j += 1
            length = int(s[idx:j])
            idx = j + 1
            out.append(s[idx: idx+length])
            idx = idx + length

        return out
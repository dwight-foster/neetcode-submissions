class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in range(len(strs)):
            word = [0 for i in range(26)]

            for s in strs[i]:
                word[(ord(s) -97)] += 1
            groups[tuple(word)].append(strs[i])
        return list(groups.values())
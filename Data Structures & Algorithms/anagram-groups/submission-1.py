class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in range(len(strs)):
            sort = ''.join(sorted(strs[i]))
            normal = strs[i]
            groups[sort].append(normal)
        
        return list(groups.values())
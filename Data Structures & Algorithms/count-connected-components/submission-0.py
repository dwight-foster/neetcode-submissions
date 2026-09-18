class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for edge1, edge2 in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)

        def dfs(edge):
            if edge in visited:
                return 
            
            visited.add(edge)
            for e in graph[edge]:
                dfs(e)
            return 
        num = 0
        for edge in range(n):
            if edge not in visited:
                num += 1
                dfs(edge)
        return num

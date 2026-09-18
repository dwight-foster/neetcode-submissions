class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()

        for e1, e2 in edges:
            graph[e1].append(e2)
        def dfs(edge):
            if edge in visited:
                return False

            if edge > n:
                return True
            visited.add(edge)
            for e in graph[edge]:
                if not dfs(e):
                    return False
            return True
        maxvisited = 0
        for edge in range(n):
            visited = set()
            if not dfs(edge):
                return False
            maxvisited = max(maxvisited, len(visited))
        print(maxvisited, len(graph))
        if maxvisited < len(graph)-1:
            return False
        return True

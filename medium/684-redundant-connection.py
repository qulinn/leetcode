class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        
        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(nei, target) for nei in graph[source])
        
        for u,v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u,v):
                return u,v
            graph[u].add(v)
            graph[v].add(u)


        # edges = [[1,2],[1,3],[2,3]]
        # ---
        # u,v = 1,2
        # u,v not in graph
        # graph[u] = {v}
        # graph[v] = {u}
        # ---
        # u,v = 1,3
        # u in graph
        # v not in graph
        # graph[u] = {v}
        # graph[v] = {u}
        # ---
        # u,v = 2,3
        # u,v in graph
        # dfs(source=u, target=v):
        #     source not in seen (seen = {})
        #     seen = {u}
        #     return [graph[source]=1, target=3]


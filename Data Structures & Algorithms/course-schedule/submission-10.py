class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if graph[node] == []:
                return True
            
            visiting.add(node)

            for pre in graph[node]:
                if not dfs(pre):
                    return False
            visiting.remove(node)
            graph[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
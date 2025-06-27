from typing import List
'''
class CourseScheduleDFS:
    def can_finish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build adjacency list
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # Step 2: 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * numCourses

        # Step 3: DFS with cycle detection
        def dfs(course):
            if visited[course] == 1:
                return False  # cycle
            if visited[course] == 2:
                return True   # already checked

            visited[course] = 1  # mark as visiting
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 2  # mark as safe
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False  # cycle found
        return True  # all courses can be completed

cs = CourseScheduleDFS()
print(cs.can_finish(numCourses = 4,prerequisites = [[1,0],[2,1],[3,2]]))

'''

from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order if len(topo_order) == numCourses else []


print(findOrder(numCourses = 4,prerequisites = [[1,0],[2,1],[3,2]]))
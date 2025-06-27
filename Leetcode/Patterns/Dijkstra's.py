import heapq
from collections import defaultdict

def dijkstra(n, edges, src):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    min_heap = [(0, src)]  # (distance, node)
    dist = [float('inf')] * n
    dist[src] = 0

    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)

        if curr_dist > dist[node]:
            continue  # Already found a shorter path

        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return dist

edges = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 4, 3)
]

print(dijkstra(5, edges, 0))

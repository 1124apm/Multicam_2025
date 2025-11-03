import heapq
# 우선순위 큐(priority queue)
# : 선입선출(first in first out)이지만, 빨리 보내야 하는 건 앞으로 보내기도 함

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    priority_queue = [(0, start_node)]

    # priority_queue에 돌아갈 게 있는 동안
    while priority_queue:
        print("="*50)
        current_distance, current_node = heapq.heappop(priority_queue)
        print(current_distance, current_node)

        if current_distance > distances[current_node]:
            print("continue")
            continue
    
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                print("push", distance, neighbor)
    
    return distances


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print(f"시작 노드: {start_node}")
print("최단 거리 결과:\n", shortest_distances)

# ==================================================
# 0 A
# push 1 B
# push 4 C
# ==================================================
# 1 B
# push 3 C
# push 6 D
# ==================================================
# 3 C
# push 4 D
# ==================================================
# 4 C
# continue      이전 C는 3이므로 4인 C는 필요없어서 continue
# ==================================================
# 4 D
# push 7 E
# ==================================================
# 6 D
# continue      이전 D는 4이므로 6인 D는 필요없어서 continue
# ==================================================
# 7 E
# 시작 노드: A
# 최단 거리 결과:
#  {'A': 0, 'B': 1, 'C': 3, 'D': 4, 'E': 7}
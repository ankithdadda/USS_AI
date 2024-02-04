import heapq

def ucs(graph, start, goal):
    visited = set()
    priority_queue = [(0, start, [])]  # Include the path in the priority queue
    path_dict = {start: None}  # Dictionary to keep track of the path

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        path = path + [node]  # Append the current node to the path

        if node == goal:
            print("Path found with cost:", cost)
            print("Path:", "->".join(path))
            return

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path))

    print("No path found.")

graph = {
    'A': [('B', 80), ('C', 99)],
    'B': [('D', 97), ('A', 80)],
    'C': [('E', 211), ('A', 99)],
    'D': [('E', 101), ('B', 97)],
    'E': [("D", 101), ("C", 211)]
}

start_node, goal_node = 'A', 'E'

print("Uniform Cost Search from", start_node, "to", goal_node)
ucs(graph, start_node, goal_node)
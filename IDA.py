import sys

def ida_star(graph, start, goal, heuristic):
    threshold = heuristic(start, goal)
    
    while True:
        response = depth_limited_search(graph, start, goal, threshold, 0, [start], heuristic)
        if type(response) is tuple:
            path, cost = response
            print("Goal reached within cost threshold.")
            print("Path:", path)
            print("Path Cost:", cost)
            return path, cost
        threshold = response

def depth_limited_search(graph, node, goal, threshold, accumulated_cost, path, heuristic):
    if node == goal:
        return path, accumulated_cost

    estimated_cost = accumulated_cost + heuristic(node, goal)
    if estimated_cost > threshold:
        return estimated_cost

    min_exceeded_threshold = sys.maxsize
    for neighbor, edge_cost in graph.get(node, []):
        if neighbor not in path:  # Avoid cycles
            new_cost = accumulated_cost + edge_cost
            path.append(neighbor)
            response = depth_limited_search(graph, neighbor, goal, threshold, new_cost, path, heuristic)
            if type(response) is tuple:
                return response
            if response < min_exceeded_threshold:
                min_exceeded_threshold = response
            path.pop()  # Backtrack

    return min_exceeded_threshold

# Example heuristic function (Manhattan distance)
def heuristic(node, goal):
    # Replace with actual heuristic calculation if needed
    positions = {'A': (0, 0), 'B': (1, 0), 'C': (0, 1), 'D': (1, 1), 'E': (2, 1), 'F': (1, 2), 'G': (2, 2)}
    node_pos = positions[node]
    goal_pos = positions[goal]
    return abs(node_pos[0] - goal_pos[0]) + abs(node_pos[1] - goal_pos[1])

# Define the graph with edge costs
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 3), ('E', 4)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 1)],  # Goal node added for demonstration
    'F': [],
    'G': []  # Goal node
}

start_node = 'A'
goal_node = 'G'

print("Iterative Deepening A* Search from", start_node, "to", goal_node)
ida_star(graph, start_node, goal_node, heuristic)
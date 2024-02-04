import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(heuristic(start, goal), start)]

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            print("Goal reached:", current_node)
            return

        if current_node not in visited:
            print("Visiting:", current_node)
            visited.add(current_node)

            neighbors = graph[current_node]
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    priority = heuristic(neighbor, goal)
                    heapq.heappush(priority_queue, (priority, neighbor))

    print("Goal not reached.")

graph = {
    'A': [('B', 11), ("C", 14), ('D', 7)],
    'B': [('E', 15), ('A', 11)],
    'C': [('E', 8), ('F', 10), ('A', 14)],
    'D': [('F', 25), ('A', 7)],
    'E': [('H', 9), ('B', 15), ('C', 8)],
    'F': [('C', 10), ('D', 25), ('G', 20)],
    'H': [('E', 9), ('G', 10)],
    'G': [('H', 10), ('F', 20)],
}

start_node = 'A'
goal_node = 'G'

heuristic_values = {}
for node in graph.keys():
    heuristic_values[node] = int(input(f"Enter heuristic value for {node} from {goal_node}: "))

def heuristic(node, goal):
    return heuristic_values[node]

print("Greedy Best-First Search from", start_node, "to", goal_node)
greedy_best_first_search(graph, start_node, goal_node, heuristic)
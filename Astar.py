import heapq

def astar(start, goal):
    graph = {
        'A': {'B': 5, 'C': 3},
        'B': {'A': 5, 'D': 2},
        'C': {'A': 3, 'D': 4, 'E': 7},
        'D': {'B': 2, 'C': 4, 'F': 6},
        'E': {'C': 7, 'F': 8},
        'F': {'D': 6, 'E': 8}
    }

    heuristic_values = {'A': 10, 'B': 8, 'C': 7, 'D': 6, 'E': 4, 'F': 0}

    open_set = [(heuristic_values[start], start)]
    closed_set = set()
    came_from = {}
    g_score = {start: 0}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            cost = g_score[goal]
            return path, cost

        closed_set.add(current)

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost

            if neighbor in closed_set and tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (g_score[neighbor] + heuristic_values[neighbor], neighbor))

    return None, float('inf')

def reconstruct_path(came_from, start, goal):
    path = [goal]
    while goal != start:
        goal = came_from[goal]
        path.insert(0, goal)
    return path

# Example usage
start_node, goal_node = 'A', 'F'
path, cost = astar(start_node, goal_node)

if path:
    print(" -> ".join(path))
    print("Cost:", cost)
else:
    print("No path found.")

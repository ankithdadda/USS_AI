# Depth-First Search (DFS) is a graph traversal 
# algorithm that explores as far as possible along
# each branch before backtracking. It is often 
# used to traverse or search through graph or 
# tree structures.

# Time Complexity:
# The time complexity of DFS is O(V + E)

#Disadvantages of DFS:

# Space Complexity
# DFS does not guarantee the optimal solution 
# Memory Usage
# cannot work on Cyclic Graphs

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : [],
  'F' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search traversal from vertex A")
dfs(visited, graph, 'A')

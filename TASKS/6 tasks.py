from collections import deque

def breadth_first_search(graph, start_node, max_depth=None):
    visited = set()  # To track visited nodes
    node_queue = deque([(start_node, 0)])  # Store node and depth in queue
    
    while node_queue:
        current_node, depth = node_queue.popleft()
        
        if current_node not in visited:
            print(f"Node: {current_node} at Depth: {depth}")
            visited.add(current_node)
            
            if max_depth is None or depth < max_depth:
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        node_queue.append((neighbor, depth + 1))

# Graph representation
graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform BFS from node 'A' with a max depth of 2
breadth_first_search(graph_data, 'A', max_depth=2)

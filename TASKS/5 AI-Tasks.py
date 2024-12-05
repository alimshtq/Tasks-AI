class GraphNode:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_connection(self, node):
        self.neighbors.append(node)

def dfs_traverse(start_node, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes
    if start_node not in visited:
        print(start_node.name)
        visited.add(start_node)  # Mark the current node as visited
        
        # Sort neighbors alphabetically to show DFS traversal order
        for neighbor in sorted(start_node.neighbors, key=lambda x: x.name):
            if neighbor not in visited:
                dfs_traverse(neighbor, visited)

# Creating graph nodes (renaming for clarity)
node_a = GraphNode('A')
node_b = GraphNode('B')
node_c = GraphNode('C')
node_d = GraphNode('D')
node_e = GraphNode('E')

# Connecting nodes (method renamed for clarity)
node_a.add_connection(node_b)
node_a.add_connection(node_c)
node_b.add_connection(node_d)
node_c.add_connection(node_e)
node_d.add_connection(node_a)  # Adding a back edge
node_e.add_connection(node_b)

print("DFS Traversal Starting from Node A:")
dfs_traverse(node_a)

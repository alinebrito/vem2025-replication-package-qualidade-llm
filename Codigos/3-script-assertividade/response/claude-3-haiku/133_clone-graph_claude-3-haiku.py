class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # Create a dictionary to store the visited nodes
        visited = {}
        
        # Define a helper function to perform the deep copy
        def dfs(n):
            # If the node has already been visited, return the copy
            if n in visited:
                return visited[n]
            
            # Create a new node with the same value
            copy = Node(n.val)
            visited[n] = copy
            
            # Recursively copy the neighbors
            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        # Start the deep copy from the given node
        return dfs(node)
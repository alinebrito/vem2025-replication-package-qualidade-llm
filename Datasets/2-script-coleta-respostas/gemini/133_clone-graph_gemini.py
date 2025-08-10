class Solution:
    def cloneGraph1(self, node):
        if not node:
            return None
        
        nodes = {}
        queue = [node]
        visited = set([node])
        
        while queue:
            curr = queue.pop(0)
            new_node = Node(curr.val, [])
            nodes[curr] = new_node
            
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        for old_node in nodes:
            for neighbor in old_node.neighbors:
                nodes[old_node].neighbors.append(nodes[neighbor])
                
        return nodes[node]
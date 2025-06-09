
class Solution:
    

  def cloneGraph(self, node):
      if not node:
          return None

      visited = {}
      queue = deque([node])

      
      visited[node] = Node(node.val)

      while queue:
          curr_node = queue.popleft()

          for neighbor in curr_node.neighbors:
              if neighbor not in visited:
                  visited[neighbor] = Node(neighbor.val)
                  queue.append(neighbor)
              visited[curr_node].neighbors.append(visited[neighbor])
      return visited[node]
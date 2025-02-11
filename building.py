from collections import deque

class Building:
    def __init__(self, id, points, warehouse):
        self.id = id
        self.points = set(points)
        self.warehouse = warehouse

    def is_valid(self):
        """Checks if the building is contiguous."""
        if not self.points:
            return False
        
        start = next(iter(self.points))
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
        
        while queue:
            current = queue.popleft()
            for dx, dy in directions:
                neighbor = (current[0] + dx, current[1] + dy)
                if neighbor in self.points and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return len(visited) == len(self.points)
import graphviz
from building import Building
from road import Road
from collections import deque

class GridParser:
    def __init__(self):
        self.buildings = {}
        self.roads = []

    def parse_buildings(self, grid, warehouse):
        """Parses the buildings from the grid and adds them to the buildings list"""
        height, width = len(grid), len(grid[0])

        #Iterates over all cells in grid
        for r in range(height):
            for c in range(width):
                if isinstance(grid[r][c], int): # Buildings    
                    #Building ID not in dictionary yet
                    if grid[r][c] not in self.buildings:
                        self.buildings[grid[r][c]] = Building(grid[r][c], [], grid[r][c] in warehouse)
                    #Add point to list of points of the building
                    self.buildings[grid[r][c]].points.add((r, c))


    def parse_roads(self, grid):
        """Parses the roads from the grid and adds them to the roads list"""
        rows, cols = len(grid), len(grid[0])
        road_id = 1  # Start numbering roads from 1
        road_map = [[None for _ in range(cols)] for _ in range(rows)]
        visited = set()
        
        def search(r, c, road_width):
            """Search to explore a continuous road segment of the same width."""
            queue = deque([(r, c)])
            visited.add((r, c))
            road_map[r][c] = road_id
            segment = [(r, c)]

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:  
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                        if grid[nx][ny] == "R":
                            # Check if the width is consistent
                            n_road_width = 1
                            for i in range(cols - ny):
                                if grid[nx][ny+i] == "R":
                                    n_road_width += 1
                                else:
                                    break
                            for i in reversed(range(ny)):
                                if grid[nx][i] == "R":
                                    n_road_width += 1
                                else:
                                    break
                            # The width is consistent so add the new row tile to the road
                            if n_road_width == road_width:
                                visited.add((nx, ny))
                                road_map[nx][ny] = road_id
                                queue.append((nx, ny))
                                segment.append((nx, ny))
            
            self.roads.append(Road(road_id, segment, road_width-1))
        
        # Identify and label roads
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "R" and (r, c) not in visited:
                    # Determine road width at this row
                    road_width = 1
                    for i in range(cols - c):
                        if grid[r][c+i] == "R":
                            road_width += 1
                        else:
                            break
                    for i in reversed(range(c)):
                        if grid[r][i] == "R":
                            road_width += 1
                        else:
                            break
                    search(r, c, road_width)
                    road_id += 1
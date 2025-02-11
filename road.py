class Road:
    def __init__(self, id, points, width, orientation):
        self.id = id
        self.points = set(points)
        self.width = width
        #0 when north-south and 1 when west-east
        self.orientation = orientation
        self.connects_to_building = []
        self.connects_to_road = []

    def is_connected(self, other):
        """Checks if two roads (or a road and a building) are connected."""
        for (r, c) in self.points:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if (nr, nc) in other.points:
                    return True
        return False
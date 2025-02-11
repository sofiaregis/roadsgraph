import graphviz
import re

class GraphGenerator:
    def __init__(self):
        self.graph = graphviz.Graph("Roads Graph")

    def create_building_nodes(self, buildings):
        """Adds the building nodes to the graph"""
        for i in sorted(buildings.keys()):
            if buildings[i].warehouse:
                self.graph.node(f"B{buildings[i].id}", f"Building {buildings[i].id} (warehouse)")
            else:
                self.graph.node(f"B{buildings[i].id}", f"Building {buildings[i].id}")

    def connect_roads_to_buildings(self, buildings, roads):
        """Adds the road segment nodes that are connected to a building (and the edges that connects them)"""
        for i in sorted(buildings.keys()):
            for road in roads:
                if road.is_connected(buildings[i]):
                    self.graph.node(f"B{buildings[i].id}_R{road.id}", f"Road {road.id} segment in Building {buildings[i].id}")
                    self.graph.edge(f"B{buildings[i].id}", f"B{buildings[i].id}_R{road.id}", label=f"{str(road.width)}")
                    road.connects_to_building.append(buildings[i].id)
            
    def create_road_nodes(self, roads):
        """Adds the road width change and intersection nodes"""
        
        r = list(roads)
        while len(r) > 0:
            road = r.pop(0)
            for other in r:

                if road.is_connected(other):
                    road.connects_to_road.append(other)
                    other.connects_to_road.append(road)
                    #The roads are connected and have the same orientation so it's a width change
                    if road.orientation == other.orientation:
                        self.graph.node(f"R{road.id}_R{other.id}", f"Road {road.id} changed width and became Road {other.id}")

                    else: #The roads don't have the same orientation so it's an intersection
                        self.graph.node(f"R{road.id}_R{other.id}", f"Road {road.id} intersects Road {other.id}")

    def connect_road_nodes(self, roads, buildings):
        """Connects rode nodes to eachother"""
        pattern = re.compile(r'\b(R\d+_R\d+)\b')
        road_pairs = pattern.findall(self.graph.source)

        for road in roads:
            #Connect road node to road nodes their connections are connected to
            for other in road.connects_to_road:
                for end in other.connects_to_road:
                    if f"R{road.id}_R{other.id}" in set(road_pairs) and f"R{other.id}_R{end.id}" in set(road_pairs):
                        pass
                        self.graph.edge(f"R{road.id}_R{other.id}", f"R{other.id}_R{end.id}", label=f"{str(other.width)}")

            #Connect road node to building road node
            for b in road.connects_to_building:
                a = [s for s in road_pairs if f"R{road.id}" in s][0]
                self.graph.edge(f"B{b}_R{road.id}", f"{a}", label=f"{str(road.width)}")
        
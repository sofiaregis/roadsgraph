import argparse, sys
from grid import Grid
from gridparser import GridParser
from graphgenerator import GraphGenerator

def main():
    grid = Grid()
    gridparser = GridParser()
    graphgenerator = GraphGenerator()

    parser = argparse.ArgumentParser(
        description="Parses a Grid in CSV format containing positional information of buildings and roads, generating a graph in .dot format"
    )
    
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Enable verbose output"
    )

    parser.add_argument(
        "-c", "--csv", type=str,
        help="Filename of the Grid CSV file."
    )

    parser.add_argument(
        "-i", "--image", type=str,
        help="Filename of the image file to be generated based on the Grid"
    )

    parser.add_argument(
        "-w", "--warehouse", type=str,
        help="Filename of the TXT file that contains IDs of buildings which are a warehouse"
    )

    parser.add_argument(
        "-g", "--graph", type=str,
        help="Filename of the graph .dot file to be generated based on the Grid"
    )
    
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
        return
    
    if args.verbose:
        print("Verbose mode enabled")


    if args.warehouse is not None:
        with open(args.warehouse) as warehousefile:
            grid.warehouse = list(map(int, warehousefile.readlines()))
        if args.verbose:
            print(f"Buildings that are a warehouse: {grid.warehouse}")
    
    if args.csv is not None:
        grid.load_from_csv(args.csv)
        gridparser.parse_buildings(grid.grid, grid.warehouse)
        for i in sorted(gridparser.buildings.keys()):
            if not gridparser.buildings[i].is_valid():
                print("ERROR: At least one building is not valid (not contiguous), exiting...", file=sys.stderr)
                return -1
        gridparser.parse_roads(grid.grid)
        if args.verbose:
            grid.display()
            print("Roads:")
            for road in gridparser.roads:
                print(f"Road {road.id}: {road.points},  width: {road.width}, orientation: {'N-S' if road.orientation == 0 else 'W-E'}")
            for i in sorted(gridparser.buildings.keys()):
                print(f"Building {gridparser.buildings[i].id}: {gridparser.buildings[i].points}, warehouse: {gridparser.buildings[i].warehouse}")
        
        if args.image is not None:
            grid.save_grid_as_image(args.verbose, args.image)

        if args.graph is not None:
            graphgenerator.create_building_nodes(gridparser.buildings)
            graphgenerator.connect_roads_to_buildings(gridparser.buildings, gridparser.roads)
            #graphgenerator.connect_roads_to_roads(gridparser.roads)
            graphgenerator.create_road_nodes(gridparser.roads)
            graphgenerator.connect_road_nodes(gridparser.roads, gridparser.buildings)

            if args.verbose:
                print(graphgenerator.graph.source)
                graphgenerator.graph.render(args.graph, view=True)
            else:
                graphgenerator.graph.render(args.graph)


if __name__ == "__main__":
    main()

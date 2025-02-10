import argparse, sys
from grid import Grid

def main():
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
        "-g", "--graph", type=str,
        help="Filename of the graph file to be generated based on the Grid"
    )

    parser.add_argument(
        "-s", "--svg", type=str,
        help="Filename of the SVG file to be generated based on the .dot graphviz format"
    )
    
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
        return
    
    if args.verbose:
        print("Verbose mode enabled")

    
    grid = Grid()
    if args.csv is not None:
        grid.load_from_csv(args.csv)
        if args.verbose:
            grid.display()

    if args.image is not None:
        grid.save_grid_as_image(args.verbose, args.image)


if __name__ == "__main__":
    main()

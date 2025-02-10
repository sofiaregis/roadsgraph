# Roads Graph

## Description

Parses a Grid in CSV format containing positional information of buildings (uniquely identified with integer IDs) and roads. Generates Graph using Graphviz that displays information on building connections to roads, connection between roads, changes in road widths, and road ends, which is then later converted to SVG.

## Features

- Parse the Grid CSV file and print it to the console.
- Generate and display PNG image from Grid CSV file, for better visualization.
- Generate Graph using Graphviz format
- Render Graph into SVG and display it

## Grid CSV Definition

Each position in the Grid is identified by it's position in a CSV file. The position can contain an integer that represents a building (and it's ID), a letter R that represents a road, or a dot (.) that represents an empty space.

Example CSV Grid file:

```csv
.,.,.,.,.,.,R,2,2,.,.
.,.,.,.,.,.,R,2,2,.,.
1,1,1,.,.,R,R,.,.,.,.
1,1,1,.,.,R,R,.,.,.,.
.,R,R,R,R,R,R,R,R,R,.
.,.,.,.,.,R,R,.,.,R,.
.,.,.,.,.,R,R,.,.,R,.
.,.,.,.,.,R,R,.,.,R,.
.,R,R,R,R,R,R,.,.,R,.
.,.,.,.,.,R,R,.,R,R,R
.,.,.,.,.,R,R,.,R,R,R
.,.,.,.,.,R,.,.,R,R,R
3,3,.,.,.,R,.,.,R,R,.
3,3,.,.,.,R,.,.,R,R,.
3,3,R,R,R,R,.,.,R,R,.
3,3,.,.,.,.,.,.,R,.,.
.,.,.,.,.,.,.,.,R,.,.
.,.,.,.,.,.,.,.,R,.,.
.,.,.,.,.,.,.,4,4,4,.
.,.,.,.,.,.,.,4,4,4,.
.,.,.,.,.,.,.,4,4,4,.
```

## Installation

### Prerequisites

Make sure you have installed: 

- Python, you can download it from [python.org](https://www.python.org/).

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/sofiaregis/roadsgraph.git
   cd roadsgraph
   ```
2. Create and activate a virtual environment (recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

The project can be ran as such:

```sh
usage: python main.py [-h] [-v] [-g GRID] [-i IMAGE]

Parses a Grid in CSV format containing positional information of buildings and roads, generating a graph in .dot format

options:
  -h, --help              show this help message and exit
  -v, --verbose           Enable verbose output
  -g GRID, --grid GRID    Filename of the Grid CSV file.
  -i IMAGE, --image IMAGE Filename of the image file to be generated based on the Grid
```

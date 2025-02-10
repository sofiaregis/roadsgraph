# Roads Graph

## Description

Parses a Grid in CSV format containing positional information of buildings (uniquely identified with integer IDs) and roads. Generates Graph in .dot file format (Graphviz) that displays information on building connections to roads, connection between roads, changes in road widths, and road ends, which is then later converted to SVG using Graphviz to be displayed. 

## Features

- Parse the Grid CSV file and print it to the console.
- Generate and display PNG image from Grid CSV file, for better visualization.
- Generate Graph in .dot file format
- Convert .dot file format into SVG and display it

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

- Graphviz, you can download it from [graphviz.org](https://graphviz.org/) (Don't forget to add Graphviz to your PATH so it can be called from the CLI, if you don't do that the automatic conversion of the .dot file into SVG won't work and you'll need to do it manually)


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
#TODO
python main.py
```

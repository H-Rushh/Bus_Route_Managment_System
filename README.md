# Bus Route Management System

A beginner-friendly Python 3 console project that stores a bus network in a dictionary, displays the direct connections of a stop, and finds a route with the **fewest stops** using Breadth First Search (BFS).

## Project details

- **Project title:** Bus Route Management System
- **Course:** B.Tech Computer Science and Engineering
- **Language:** Python 3
- **Main concepts:** Lists, dictionaries, functions, loops, and graph traversal (BFS)
- **Fare:** Rs. 1.50 per kilometre

## Features

1. Displays the direct connections and distances for a selected bus stop.
2. Finds a route with the fewest stops between two stops using BFS.
3. Calculates the total distance of the selected route.
4. Calculates the fare using `fare = distance * 1.50`.
5. Handles an unknown stop, a route that is not available, and the case where source and destination are the same.
6. Stores each road in both directions.

## Bus network

| Connected stops | Distance |
|---|---:|
| Durg - Bhilai | 10 km |
| Bhilai - Raipur | 30 km |
| Durg - Raipur | 40 km |
| Raipur - Bilaspur | 110 km |
| Raipur - Dhamtari | 80 km |
| Durg - Rajnandgaon | 45 km |
| Jagdalpur - Kondagaon | 75 km |

Jagdalpur and Kondagaon form a separate connection and are not connected to the other stops.

## Requirements

- Python 3 installed on your computer
- Any code editor or terminal (for example, VS Code)

No external Python libraries are required.

## How to run

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run:

   ```bash
   python one.py
   ```

   On some systems, use `python3 one.py` instead.
4. Select an option from the menu:
   - `1` - Show Connections
   - `2` - Find Route
   - `3` - Exit

Enter stop names with the same spelling and capitalization as shown in the bus network (for example, `Raipur`).

## How the route search works

The program uses Breadth First Search (BFS). It starts from the source stop and checks neighbouring stops level by level. The first time the destination is reached, the path contains the fewest road connections (and therefore the fewest stops, counting the source and destination). The program then adds the distances along that path and calculates the fare.

**Note:** BFS finds the route with the fewest connections; it does not necessarily find the route with the minimum kilometre distance when different routes have different road lengths.

## Test cases

The project was checked against the four cases in the assignment:

| Test case | Input | Expected result |
|---|---|---|
| 1. Normal input | Show connections for Raipur | Bhilai (30 km), Bilaspur (110 km), Dhamtari (80 km), Durg (40 km) |
| 2. Boundary / minimum input | Find route from Durg to Durg | Same source and destination; 0 km; Rs. 0.00 |
| 3. Invalid / unavailable input | Durg to Jagdalpur; show connections for Delhi | No route between Durg and Jagdalpur; Delhi is not found |
| 4. Different valid scenario | Bhilai to Bilaspur | Bhilai -> Raipur -> Bilaspur; 3 stops; 140 km; Rs. 210.00 |

The console output screenshots are included in [`Summary.md`](Summary.md) and the [`screenshot/`](screenshot/)folder.

## Repository files

```text
bus-route-management/
├── one.py
├── README.md
├── Summary.md
└── screenshot/
    ├── Test_Case_1.png
    ├── Test_Case_2.png
    ├── Test_Case_3.png
    └── Test_Case_4.png
```

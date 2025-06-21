
# Flight Planner

This repository contains a Flight Planner system developed as part of the COL106 Assignment 5 (November 2024). The planner reads flight schedules and computes optimal itineraries based on different criteria.

## Features

1. **Fewest Flights & Earliest Arrival** (`least_flights_earliest_route`)
2. **Cheapest Trip** (`cheapest_route`)
3. **Fewest Flights & Cheapest** (`least_flights_cheapest_route`)

Each route-finding method considers a departure-time window `[t1, t2]` and a mandatory minimum connection time of 20 minutes between consecutive flights.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/flight-planner.git
   cd flight-planner
2. Ensure you have Python 3.7+ installed.

No external dependencies are required beyond the standard library.

## Project Structure

```
flight-planner/
├── Code/
│   ├── flight.py         # Flight class, heap, and queue implementations
│   └── planner.py        # Planner class with three route-finding methods
├── main.py               # Example usage and basic tests
├── COL106_A5.pdf         # Assignment specification
└── README.md             # Project overview and instructions
```

## File Descriptions

* **Code/flight.py**

  * Defines the `Flight` model and utility data structures:

    * `Heap` (min-heap with customizable comparison)
    * `LinkedListQueue` (FIFO queue)
* **Code/planner.py**

  * Implements `Planner` with three optimization methods:

    1. `least_flights_earliest_route(start, end, t1, t2)`
    2. `cheapest_route(start, end, t1, t2)`
    3. `least_flights_cheapest_route(start, end, t1, t2)`
* **main.py**

  * Demonstrates the planner on a sample network of flights and prints pass/fail for each task.
* **COL106\_A5.pdf**

  * Original assignment description and requirements.

## Usage

Run the example in `main.py`:

```bash
python main.py
```

To integrate into your own code, instantiate the planner:

```python
from Code.flight import Flight
from Code.planner import Planner

# Load or define a list of Flight objects
flights = [
    Flight(0, 0, 0, 1, 30, 50),
    # ... other flights ...
]

planner = Planner(flights)
route = planner.cheapest_route(start_city=0, end_city=4, t1=0, t2=300)
for f in route:
    print(f"Flight {f.flight_no}: {f.start_city}->{f.end_city} departs at {f.departure_time} arrives at {f.arrival_time} cost {f.fare}")
```

Modify parameters `start_city`, `end_city`, `t1`, and `t2` as needed.

## Performance

* `__init__`:		O(m) where m = number of flights
* `least_flights_earliest_route`:	O(m)
* `cheapest_route`:	O(m log m)
* `least_flights_cheapest_route`:	O(m log m)

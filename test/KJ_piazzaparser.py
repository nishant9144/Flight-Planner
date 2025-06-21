from Code.flight import Flight
from Code.planner import Planner

def parse_test_case(file_path):
    with open(file_path, 'r') as file:
        n, m = map(int, file.readline().strip().split())  # Read number of vertices and edges
        flights = []
        
        for _ in range(m):
            u, v, cost, start_time, end_time = map(int, file.readline().strip().split())
            flight = Flight(len(flights), u, start_time, v, end_time, cost)
            flights.append(flight)
    
    return flights

def main():
    file_path = 'C.txt'
    flights = parse_test_case(file_path) 
    flight_planner = Planner(flights)
    
    # Test case for start_city=0, destination=100, and destination=110
    start_city = 0
    destinations = [100, 110]
    
    for destination in destinations:
        print(f"\nTesting routes for start_city={start_city}, destination={destination}")
        
        # Task 1: Least Flights Earliest Route
        route1 = flight_planner.least_flights_ealiest_route(start_city, destination, 0, 100000000)
        if route1:
            num_flights_task1 = len(route1)
            arrival_time_task1 = route1[-1].arrival_time if num_flights_task1 > 0 else None
            print(f"Task 1: Least Flights Earliest Route - Number of flights: {num_flights_task1}, Arrival time: {arrival_time_task1}")
        else:
            print("Task 1: No route found.")
        
        # Task 2: Cheapest Route
        route2 = flight_planner.cheapest_route(start_city, destination, 0, 10000000000)
        if route2:
            total_cost_task2 = sum(flight.fare for flight in route2)
            print(f"Task 2: Cheapest Route - Total cost: {total_cost_task2}")
        else:
            print("Task 2: No route found.")
        
        # Task 3: Least Flights Cheapest Route
        route3 = flight_planner.least_flights_cheapest_route(start_city, destination, 0, 1000000000)
        if route3:
            num_flights_task3 = len(route3)
            total_cost_task3 = sum(flight.fare for flight in route3)
            print(f"Task 3: Least Flights Cheapest Route - Number of flights: {num_flights_task3}, Total cost: {total_cost_task3}")
        else:
            print("Task 3: No route found.")

if __name__ == "__main__":
    main()

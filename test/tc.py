from Code.flight import Flight
from Code.planner import Planner
def main():
    flights = [Flight(0, 0, 100, 1, 190, 500),
               Flight(1, 0, 5, 7, 6, 2000),
               Flight(2, 5, 90, 0, 100, 1000),
               Flight(3, 5, 47, 2, 48, 1000),
               Flight(4, 5, 90, 6, 100, 1500),
               Flight(5, 7, 26, 5, 27, 500),
               Flight(6, 6, 120, 7, 140, 1000),
               Flight(7, 2, 150, 6, 200, 1000),
               Flight(8, 6, 20, 4, 40, 500),
               Flight(9, 2, 68, 9, 70, 1000),
               Flight(10, 1, 210, 9, 300, 500),
               Flight(11, 8, 115, 4, 200, 3000),
               Flight(12, 9, 380, 3, 400, 500),
               Flight(13, 9, 90, 8, 95, 2000),
               Flight(14, 6, 220, 4, 240, 2500),
               Flight(15, 7, 10, 4, 30, 5000),
               Flight(16, 0, 0, 8, 100, 600),#
               Flight(17, 8, 130, 1, 200, 400),                              
               Flight(18, 1, 200, 2, 300, 1500),
               Flight(19, 2, 320, 3, 340, 500),
               Flight(20, 3, 380, 4, 400, 2000),
               ]
    
    flight_planner = Planner(flights)
    # The three tasks
    route1 = flight_planner.least_flights_ealiest_route(0, 4, 0, 500)
    route2 = flight_planner.cheapest_route(0, 4, 0, 500)
    route3 = flight_planner.least_flights_cheapest_route(0, 4, 0, 500)

    print("\nActual Route1 :")
    for flight in route1:
        print(f"Flight No: {flight.flight_no}, Start City: {flight.start_city}, "
              f"Departure Time: {flight.departure_time}, End City: {flight.end_city}, "
              f"Arrival Time: {flight.arrival_time}, Fare: {flight.fare}")
        
    print("\nActual Route2 :")
    for flight in route2:
        print(f"Flight No: {flight.flight_no}, Start City: {flight.start_city}, "
              f"Departure Time: {flight.departure_time}, End City: {flight.end_city}, "
              f"Arrival Time: {flight.arrival_time}, Fare: {flight.fare}")

    print("\nActual Route3 :")
    for flight in route3:
        print(f"Flight No: {flight.flight_no}, Start City: {flight.start_city}, "
              f"Departure Time: {flight.departure_time}, End City: {flight.end_city}, "
              f"Arrival Time: {flight.arrival_time}, Fare: {flight.fare}")

if __name__ == "__main__":
    main()

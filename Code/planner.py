from Code.flight import Flight, Heap, LinkedListQueue

class Planner:
    def __init__(self, flights):
        """The Planner
        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.flights = flights
        self.no_of_cities = 0
        self.adj_list = [[] for _ in range(len(flights))]
        for flight in flights:
            self.no_of_cities = max(self.no_of_cities, flight.start_city, flight.end_city)
            self.adj_list[flight.start_city].append(flight)
    
    def least_flights_ealiest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        my_queue = LinkedListQueue()

        dp = [None for _ in range(self.no_of_cities + 1)] # stores the number of flights to reach a city
        prev_flight_array = [None for _ in range(len(self.flights))] # stores the previous flight
        my_queue.enqueue([start_city, t1, 0, None]) # city, time, number of flights, Flight name
        best_flight = None
        path = []

        if start_city == end_city:
            return path
        
        while not my_queue.is_empty():
            city, time, no_flights, name = my_queue.dequeue()

            if city == end_city:
                if best_flight == None:
                    best_flight = name
                else:
                    if no_flights < dp[end_city]:
                        best_flight = name
                        dp[end_city] = no_flights
                    elif no_flights == dp[end_city]:
                        if self.flights[name].arrival_time < self.flights[best_flight].arrival_time:
                            best_flight = name
                    if no_flights > dp[end_city]:
                        break
                continue

            for flight in self.adj_list[city]:
                if city == start_city:
                    if flight.departure_time >= time and flight.arrival_time <= t2:
                        prev_flight_array[flight.flight_no] = name
                        my_queue.enqueue([flight.end_city, flight.arrival_time, no_flights + 1, flight.flight_no])
                        dp[city] = 0
                        dp[flight.end_city] = 1
                else:
                    if flight.departure_time >= time + 20 and flight.arrival_time <= t2:
                        if prev_flight_array[flight.flight_no] == None:
                            prev_flight_array[flight.flight_no] = name
                            my_queue.enqueue([flight.end_city, flight.arrival_time, no_flights + 1, flight.flight_no])
                            dp[city] = min(dp[city], no_flights) if dp[city] != None else no_flights
                            dp[flight.end_city] = min(dp[flight.end_city], no_flights + 1) if dp[flight.end_city] != None else no_flights + 1
                        elif no_flights < dp[city]:
                            prev_flight_array[flight.flight_no] = name
                            my_queue.enqueue([flight.end_city, flight.arrival_time, no_flights + 1, flight.flight_no])
                            dp[city] = min(no_flights, dp[city]) if dp[city] != None else no_flights
                            dp[flight.end_city] = min(no_flights + 1, dp[flight.end_city]) if dp[flight.end_city] != None else no_flights + 1
            
        if best_flight == None:
            return path
    
        path.append(self.flights[best_flight])       
        while best_flight != None and self.flights[best_flight].start_city != start_city:
            curr_flight = prev_flight_array[best_flight]
            if curr_flight == None:
                break
            path.append(self.flights[curr_flight])
            best_flight = curr_flight
        
        return path[::-1]

    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        path = []
        if start_city == end_city:
            return path
        
        visited = [False for _ in range(len(self.flights) + 1)]
        priority_queue = Heap([],lambda x,y: x[1] < y[1])
        prev_flight_array = [None for _ in range(len(self.flights) + 1)] # stores the previous flight
        for flight in self.adj_list[start_city]:
            if flight.departure_time >= t1 and flight.arrival_time <= t2:
                prev_flight_array[flight.flight_no] = None
                visited[flight.flight_no] = True
                priority_queue.insert([flight, flight.fare, flight.arrival_time]) # abhi tak ka cost, flight ka landing time

        best_flight = None # last ke liye, arrival time bhi isi mein hai
        best_cost = float('inf')
        while priority_queue.size > 0: 
            flight, cost, time = priority_queue.extract()

            city = flight.end_city
            if city == end_city:
                best_flight = flight
                best_cost = cost
                break

            for departing_flight in self.adj_list[city]:
                if not visited[departing_flight.flight_no]:
                    if departing_flight.departure_time >= time + 20 and departing_flight.arrival_time <= t2:
                        prev_flight_array[departing_flight.flight_no] = flight
                        priority_queue.insert([departing_flight, cost + departing_flight.fare, departing_flight.arrival_time])
                        visited[departing_flight.flight_no] = True

        if best_flight == None:
            return path
        
        curr_flight = best_flight
        while curr_flight is not None:
            path.append(curr_flight)
            curr_flight = prev_flight_array[curr_flight.flight_no]
        return path[::-1]

    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        path = []
        if start_city == end_city:
            return path
        
        priority_queue = Heap([], lambda x, y: (x[-1],x[1]) < (y[-1],y[1]))
        dp = [float('inf') for _ in range(len(self.flights) + 1)] # stores the best fare for this city
        prev_flight_array = [None for _ in range(len(self.flights) + 1)] # stores the previous flight
        number_dp = [float('inf') for _ in range(len(self.flights)+1)] #stores waha tak pahochne ke number of flights

        for flight in self.adj_list[start_city]:
            if flight.departure_time >= t1 and flight.arrival_time <= t2:
                prev_flight_array[flight.flight_no] = None
                number_dp[flight.flight_no] = flight.fare
                priority_queue.insert([flight, flight.fare, flight.arrival_time, 0]) #object, cost flight included, arr time, num flights

        best_flight = None 
        best_cost = float('inf')
        best_number = float('inf')
        while priority_queue.size > 0: 
            flight, cost, time, num_flights = priority_queue.extract()

            city = flight.end_city
            if city == end_city:
                best_flight = flight
                best_cost = cost
                best_number = num_flights+1
                break

            for departing_flight in self.adj_list[city]:
                if departing_flight.departure_time >= time + 20 and departing_flight.arrival_time <= t2:
                    if number_dp[departing_flight.flight_no] == float('inf'):
                        dp[departing_flight.flight_no] = cost + departing_flight.fare
                        number_dp[departing_flight.flight_no] = num_flights + 1
                        prev_flight_array[departing_flight.flight_no] = flight
                        priority_queue.insert([departing_flight, cost + departing_flight.fare, departing_flight.arrival_time, num_flights + 1])

        if best_flight == None:
            return path
        
        curr_flight = best_flight
        while curr_flight is not None:
            path.append(curr_flight)
            curr_flight = prev_flight_array[curr_flight.flight_no]
        return path[::-1]
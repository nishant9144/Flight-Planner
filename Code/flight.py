class Flight:
    def __init__(self, flight_no, start_city, departure_time, end_city, arrival_time, fare):
        """ Class for the flights

        Args:
            flight_no (int): Unique ID of each flight
            start_city (int): The city no. where the flight starts
            departure_time (int): Time at which the flight starts
            end_city (int): The city no where the flight ends
            arrival_time (int): Time at which the flight ends
            fare (int): The cost of taking this flight
        """
        self.flight_no = flight_no
        self.start_city = start_city
        self.departure_time = departure_time
        self.end_city = end_city
        self.arrival_time = arrival_time
        self.fare = fare

    # def __str__(self):
    #     return f"{self.flight_no} [{self.start_city}({self.departure_time}) -> {self.end_city}({self.arrival_time})]"
    
    # def __repr__(self):
    #     return self.__str__()
        
"""
If there are n flights, and m cities:

1. Flight No. will be an integer in {0, 1, ... n-1}
2. Cities will be denoted by an integer in {0, 1, .... m-1}
3. Time is denoted by a non negative integer - we model time as going from t=0 to t=inf
"""
class Heap:
    def __init__(self, init_array,comparison_function):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''

        self.comparison_function = comparison_function
        self.heap = init_array[:]  # Create a copy of the input array
        self.size = len(init_array)
        self._build_heap()

    def _build_heap(self):
        # Heapify the array in O(n) time
        for i in range(self.size // 2 - 1, -1, -1):
            self._heapify_down(i)
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        self.heap.append(value)
        self.size += 1
        self._heapify_up(self.size - 1)
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
    
        if self.size == 0:
            return None
    
        top_value = self.heap[0]
        
        # Only replace the top with the last element if there are still elements left
        if self.size > 1:
            self.heap[0] = self.heap.pop()  # Replace the root with the last element
        else:
            self.heap.pop()  # Just remove the last element if it's the only one

        self.size -= 1
        
        # If there's still an element, heapify down
        if self.size > 0:
            self._heapify_down(0)
        
        return top_value
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        if self.size == 0:
            return None
        return self.heap[0]
    
    # You can add more functions if you want to

    def _heapify_up(self, index):
        '''
        Helper function to maintain heap property when an element is inserted.
        '''
        parent = (index - 1) // 2
        while index > 0 and self.comparison_function(self.heap[index], self.heap[parent]):
            # Swap the current element with its parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        '''
        Helper function to maintain heap property after extraction.
        '''
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        # Compare with left child
        if left_child < self.size and self.comparison_function(self.heap[left_child], self.heap[smallest]):
            smallest = left_child

        # Compare with right child
        if right_child < self.size and self.comparison_function(self.heap[right_child], self.heap[smallest]):
            smallest = right_child

        # If the current node is not the smallest, swap with the smallest child and recurse
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
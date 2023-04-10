import threading

class ResourceAllocationSystem:
    def _init_(self, n, m, available, maximum):
        self.n = n
        self.m = m
        self.available = available
        self.maximum = maximum
        self.allocation = [[0] * m for _ in range(n)]
        self.need = [[maximum[i][j] for j in range(m)] for i in range(n)]
        self.mutex = threading.Lock()

    def request_resources(self, thread_num, request):
        with self.mutex:
            if all(request[i] <= self.need[thread_num][i] for i in range(self.m)) and all(request[i] <= self.available[i] for i in range(self.m)):
                for i in range(self.m):
                    self.available[i] -= request[i]
                    self.allocation[thread_num][i] += request[i]
                    self.need[thread_num][i] -= request[i]
                return True
            else:
                return False

    def release_resources(self, thread_num, release):
        with self.mutex:
            for i in range(self.m):
                self.available[i] += release[i]
                self.allocation[thread_num][i] -= release[i]
                self.need[thread_num][i] += release[i]

    def get_available_resources(self):
        with self.mutex:
            return self.available

    def get_maximum_demand(self):
        with self.mutex:
            return self.maximum

    def get_allocation(self):
        with self.mutex:
            return self.allocation

    def get_need(self):
        with self.mutex:
            return self.need

def main():
    # Read input from user
    n = int(input("Enter the number of threads: "))
    m = int(input("Enter the number of resources: "))

    # Initialize available resources
    print("Enter the number of available resources for each type:")
    available = list(map(int, input().split()))

    # Initialize maximum demand of each thread
    print("Enter the maximum demand of each thread for each resource type:")
    maximum = [[int(x) for x in input().split()] for _ in range(n)]

    # Initialize resource allocation system
    system = ResourceAllocationSystem(n, m, available, maximum)

    # Print initial state of the system
    print("\nInitial state of the system:")
    print("Available resources:", system.get_available_resources())
    print("Maximum demand of each thread:")
    for i in range(n):
        print("Thread {}: {}".format(i, system.get_maximum_demand()[i]))
    print("Resources allocated to each thread:")
    for i in range(n):
        print("Thread {}: {}".format(i, system.get_allocation()[i]))
    print("Remaining needs of each thread:")
    for i in range(n):
        print("Thread {}: {}".format(i, system.get_need()[i]))

if _name_ == '_main_':
    main()

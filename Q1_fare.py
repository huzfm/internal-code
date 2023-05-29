class Vehicle:
    def __init__(self, capacity):
        self.capacity=capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        fare1 =self.capacity * 100
        total_fare = fare1 + (0.1 * fare1)
        return total_fare
final=Bus(5)
print(final.fare())
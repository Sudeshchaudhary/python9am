class Vehicle:
    def __init__(self, seat, fare):
        self.seat = seat
        self.fare = fare

    def fareamount(self):
        print("fare of vehicle is", self.seat * self.fare)


fare = Vehicle(50, 100)
fare.fareamount()


class Bus(Vehicle):

    def busfare(self):
        fare = self.seat * self.fare
        newfare = fare + fare * 10 / 100
        print("The fare of bus is", newfare)


fare = Bus(50, 100)
fare.busfare()

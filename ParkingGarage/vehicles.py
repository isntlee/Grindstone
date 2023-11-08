class Vehicle:
    def __init__(self, spot_size):
        self._spot_size = spot_size

    def get_spot_size(self):
        return self._spot_size
    

class Car(Vehicle):
    def __init__(self):
        super().__init__(1)


class Limo(Vehicle):
    def __init__(self):
        super().__init__(2)


class Truck(Vehicle):
    def __init__(self):
        super().__init__(3)
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # Store counts in a dictionary where keys map directly to carType values (1, 2, 3)
        self.slots = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        # Check if there is an available slot for the requested carType
        if self.slots[carType] > 0:
            self.slots[carType] -= 1  # Occupy one slot
            return True
        
        return False  # No empty slots available


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
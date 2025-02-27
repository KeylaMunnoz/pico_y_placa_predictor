#Define the LicensePlate class to represent a vehicle's license plate
class LicensePlate:
    
    def __init__(self, plate_number: str):
        self.plate_number = plate_number

    def get_last_digit(self) -> int:
        return int(self.plate_number[-1])
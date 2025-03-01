from datetime import datetime
from app.models.license_plate import LicensePlate
from app.utils.time_utils import is_restricted_time
from app.core.config import RESTRICTION_DAYS

#Function to determine if a vehicle can drive based on plate number, date, and time
def can_drive(plate: str, date_str: str, time_str: str) -> bool:
    plate_obj = LicensePlate(plate)
    last_digit = plate_obj.get_last_digit()
    restriction_days = RESTRICTION_DAYS.get(last_digit, [])
    
    #Convert the date string to a datetime object and extract the day of the week
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    day_of_week = date_obj.strftime("%A")
    
    #Check if the day and time are restricted
    if day_of_week in restriction_days and is_restricted_time(time_str):
        return False #Vehicle cannot be on road
    return True #Vehicle can be on road
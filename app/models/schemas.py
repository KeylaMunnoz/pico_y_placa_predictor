from pydantic import BaseModel, field_validator
from datetime import datetime

class PicoPlacaRequest(BaseModel):
    plate_number: str
    date: str  # YYYY-MM-DD
    time: str  # HH:MM (24-hour format)

    # Validator for the 'date' field
    @field_validator('date')
    def validate_date(cls, v):
        try:
            # Try to parse the date to validate the format
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in the format YYYY-MM-DD.")
        return v

    # Validator for the 'time' field
    @field_validator('time')
    def validate_time(cls, v):
        try:
            # Try to parse the time to validate the format
            datetime.strptime(v, "%H:%M")
        except ValueError:
            raise ValueError("Time must be in the format HH:MM (24-hour format).")
        return v

class PicoPlacaResponse(BaseModel):
    can_drive: bool
    message: str

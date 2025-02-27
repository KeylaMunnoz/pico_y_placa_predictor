from pydantic import BaseModel

# Request model for Pico y Placa validation
class PicoPlacaRequest(BaseModel):
    plate_number: str
    date: str  # YYYY-MM-DD
    time: str  # HH:MM (24-hour format)
                                          
# Response model for Pico y Placa validation result
class PicoPlacaResponse(BaseModel):
    can_drive: bool
    message: str
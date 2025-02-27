from fastapi import APIRouter, HTTPException
from app.models.schemas import PicoPlacaRequest, PicoPlacaResponse
from app.services.pico_placa import can_drive
from app.services.validator import is_valid_plate

#Defined the router for the '/predictor' endpoint, grouped under the "Pico y Placa" tag
router = APIRouter(prefix="/predictor", tags=["Pico y Placa"])

#POST request to check if a vehicle can drive based on plate number, date, and time
@router.post("/check", response_model=PicoPlacaResponse)
def check_pico_placa(request: PicoPlacaRequest):
    if not is_valid_plate(request.plate_number):
        raise HTTPException(status_code=400, detail="Invalid plate format")
    
    allowed = can_drive(request.plate_number, request.date, request.time)
    return PicoPlacaResponse(
        can_drive=allowed,
        message="Your car can be on road" if allowed else "Your car cannot be on road at this time"
    )
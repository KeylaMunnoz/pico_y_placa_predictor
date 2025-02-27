from app.models.license_plate import LicensePlate

def test_get_last_digit():
    plate = LicensePlate("ABC-1234")
    assert plate.get_last_digit() == 4
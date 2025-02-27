from app.services.pico_placa import can_drive

def test_can_drive_allowed():
    assert can_drive("ABC-1234", "2025-02-28", "10:00") == True

def test_can_drive_restricted():
    assert can_drive("ABC-1231", "2025-02-24", "08:00") == False
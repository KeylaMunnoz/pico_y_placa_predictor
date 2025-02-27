from app.services.validator import is_valid_plate

def test_valid_plate():
    assert is_valid_plate("PBC-1234") == True
    assert is_valid_plate("XYZ-999P") == False
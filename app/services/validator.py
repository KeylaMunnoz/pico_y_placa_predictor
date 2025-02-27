import re

# List of valid province letters for the first digit of the plate
VALID_PROVINCE_LETTERS = "ABUCXHOEWGILRVMNSPQKTZYJ"

def is_valid_plate(plate: str) -> bool:
    return bool(re.match(rf"^[{VALID_PROVINCE_LETTERS}][A-Z]{{2}}-\d{{3,4}}$", plate))
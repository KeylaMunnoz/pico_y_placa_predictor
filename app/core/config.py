#intervals configuration for restricted time
RESTRICTED_INTERVALS = [
    ("07:00", "09:30"),
    ("16:00", "19:30")
]

#restricted days intervals according to the last digit of the car's plate
RESTRICTION_DAYS = {
    1: ["Monday"], 2: ["Monday"],
    3: ["Tuesday"], 4: ["Tuesday"],
    5: ["Wednesday"], 6: ["Wednesday"],
    7: ["Thursday"], 8: ["Thursday"],
    9: ["Friday"], 0: ["Friday"]
}
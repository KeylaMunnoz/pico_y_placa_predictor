from datetime import datetime

def is_restricted_time(time_str: str) -> bool:
    restricted_intervals = [("07:00", "09:30"), ("16:00", "19:30")]
    time_obj = datetime.strptime(time_str, "%H:%M").time()
    
    for start, end in restricted_intervals:
        start_time = datetime.strptime(start, "%H:%M").time()
        end_time = datetime.strptime(end, "%H:%M").time()
        if start_time <= time_obj <= end_time:
            return True
    return False
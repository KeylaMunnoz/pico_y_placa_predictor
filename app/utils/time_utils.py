from datetime import datetime
from app.core.config import RESTRICTED_INTERVALS

def is_restricted_time(time_str: str) -> bool:
    time_obj = datetime.strptime(time_str, "%H:%M").time()
    
    for start, end in RESTRICTED_INTERVALS:
        start_time = datetime.strptime(start, "%H:%M").time()
        end_time = datetime.strptime(end, "%H:%M").time()
        if start_time <= time_obj <= end_time:
            return True
    return False
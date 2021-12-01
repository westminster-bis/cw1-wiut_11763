from classes import CW
from datetime import datetime

csf_cw = CW(
    deadline=datetime(2020, 12, 3, 23, 59),
    submission_time=datetime(2020, 12, 5, 4, 59)
)

print(csf_cw.is_on_time())
print(csf_cw.is_within_24_hours())
print(csf_cw.marks)
print(csf_cw.get_full_mark())


from classes import CW
from datetime import datetime, timedelta

students = [
    {
        'id': "00011111",
        'group': "4BIS11",
        'full_name': "John Doe",
        'deadline': datetime.today(),
        'submission_time': datetime.today() - timedelta(days=1),
    }
]

csf_cw = CW(
    name="CSF",
    deadline=datetime(2020, 12, 3, 23, 59),
    submission_time=datetime(2020, 12, 5, 4, 59)
)

print(csf_cw.get_full_mark())


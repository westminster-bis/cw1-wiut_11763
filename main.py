from classes import CW
from datetime import datetime, timedelta

# List of Students
students = [
    {
        'id': "00011111",
        'group': "4BIS11",
        'full_name': "John Doe",
        'module_name': "CSF",
        'deadline': datetime(2021, 12, 1, 23, 59),
        'submission_time': datetime(2021, 12, 1, 23, 59) - timedelta(days=1),
    },
    {
        'id': "00022222",
        'group': "4BIS12",
        'full_name': "Jack Michael",
        'module_name': "WebTech",
        'deadline': datetime(2021, 12, 9, 23, 59),
        'submission_time': datetime(2021, 12, 9, 23, 59) + timedelta(days=1),
    },
    {
        'id': "00033333",
        'group': "4BIS13",
        'full_name': "Eloisa Spears",
        'module_name': "FunPro",
        'deadline': datetime(2021, 12, 14, 23, 59),
        'submission_time': datetime(2021, 12, 14, 23, 59) + timedelta(days=4),
    }

]

for student in students:
    cw = CW(
        name=student['module_name'],
        deadline=student['deadline'],
        submission_time=student['submission_time'],
    )

    student.update(full_mark=cw.get_full_mark())

    message = f"{student['full_name']} \n" \
              f"ID: {student['id']}, Group: {student['group']} \n" \
              f"Module: {student['module_name']} \n" \
              f"Result: {student['full_mark']}"
    print('-'*5)
    print(message)


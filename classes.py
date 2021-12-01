from datetime import datetime, timedelta


class CW:
    ZERO_MARK = 0
    FULL_MARK = 1
    DECREASED_MARK = 2

    marks = [
        "Mark = 0",
        "Full Mark",
        "Minus 10 marks from overall marks but not below 40",
    ]

    def __init__(self, deadline: datetime, submission_time: datetime, has_valid_reason_ls, is_mc_ls_accepted):
        self.deadline = deadline
        self.submissionTime = submission_time
        self.has_valid_reason_ls = has_valid_reason_ls
        self.is_mc_ls_accepted = is_mc_ls_accepted

    def is_on_time(self):
        submission_time = self.submissionTime
        deadline = self.deadline
        return submission_time < deadline

    def is_within_24_hours(self):
        submission_time = self.submissionTime
        deadline = self.deadline
        if self.is_on_time():
            return 'invalid'
        t: datetime = submission_time - deadline
        return t < timedelta(days=1)

    def get_full_mark_category(self):
        if self.is_on_time():
            return self.FULL_MARK

        if self.is_within_24_hours():
            if self.has_valid_reason_ls and self.is_mc_ls_accepted:
                return self.FULL_MARK
            else:
                return self.DECREASED_MARK

        return self.ZERO_MARK

    def get_full_mark(self):
        mark_category = self.get_full_mark_category()
        print(mark_category)
        return self.marks[mark_category]

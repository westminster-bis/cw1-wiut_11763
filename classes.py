from datetime import datetime, timedelta


class CW:
    ZERO_MARK = 0
    FULL_MARK = 1
    DECREASED_MARK = 2
    DEFERRAL = 3

    marks = [
        "Mark = 0",
        "Full Mark",
        "Minus 10 marks from overall marks but not below 40",
        "Deferral Reassessment"
    ]

    def __init__(self, deadline: datetime, submission_time: datetime,
                 has_valid_reason_ls, is_mc_ls_accepted,
                 has_valid_reason_ls_5d_yes, is_mc_ls_option_accepted,
                 has_valid_reason_ls_5d_no, is_mc_defer_accepted):
        self.deadline = deadline
        self.submissionTime = submission_time

        self.has_valid_reason_ls = has_valid_reason_ls
        self.is_mc_ls_accepted = is_mc_ls_accepted

        self.has_valid_reason_ls_5d_yes = has_valid_reason_ls_5d_yes
        self.is_mc_ls_option_accepted = is_mc_ls_option_accepted

        self.is_mc_defer_accepted = is_mc_defer_accepted
        self.has_valid_reason_ls_5d_no = has_valid_reason_ls_5d_no

    def is_on_time(self):
        submission_time = self.submissionTime
        deadline = self.deadline
        return submission_time < deadline

    def is_within_24_hours(self):
        submission_time = self.submissionTime
        deadline = self.deadline
        interval: datetime = submission_time - deadline
        return interval <= timedelta(days=1)

    def is_within_5_days(self):
        submission_time = self.submissionTime
        deadline = self.deadline
        interval: datetime = submission_time - deadline
        return interval <= timedelta(days=5)

    def get_full_mark_category(self):
        if self.is_on_time():
            return self.FULL_MARK

        if self.is_within_24_hours():
            if self.has_valid_reason_ls and self.is_mc_ls_accepted:
                return self.FULL_MARK
            else:
                return self.DECREASED_MARK

        if self.is_within_5_days():
            if self.has_valid_reason_ls_5d_yes:
                if self.is_mc_ls_option_accepted:
                    return self.FULL_MARK
                else:
                    return self.ZERO_MARK
            else:
                return self.ZERO_MARK
        else:
            if self.has_valid_reason_ls_5d_no:
                if self.is_mc_defer_accepted:
                    return self.DEFERRAL
                else:
                    return self.ZERO_MARK
            else:
                return self.ZERO_MARK

    def get_full_mark(self):
        mark_category = self.get_full_mark_category()
        print(mark_category)
        return self.marks[mark_category]

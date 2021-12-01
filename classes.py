from datetime import datetime, timedelta


class CW:
    """
    A class used to represent a Course Work instance
    Main task: to identify the full mark for the submitted course work according to the deadline and submission time

    ...

    Attributes
    ---------
    name: str
        name of the module of the cw

    deadline: datetime
        deadline for submission

    submission_time: datetime
        time of actual submission

    has_valid_reason_ls: bool, optional
        does late submission have a valid reason?

    is_mc_ls_accepted: bool, optional
        is mitigating circumstance for late submission accepted?

    has_valid_reason_ls_5d_yes: bool, optional
        is there a valid reason of submitting within 5 days?

    is_mc_ls_option_accepted: bool, optional
        is late submitted mitigation circumstance accepted?

    has_valid_reason_ls_5d_no: bool, optional
        is there a valid reason for submitting in more than 5 days

    is_mc_defer_accepted:
        is mitigating circumstance for non-submission/deferral accepted
    """
    ZERO_MARK = 0
    FULL_MARK = 1
    DECREASED_MARK = 2
    DEFERRAL = 3

    marks = (
        "Mark = 0",
        "Full Mark",
        "Minus 10 marks from overall marks but not below 40",
        "Deferral Reassessment"
    )

    def __init__(self, name, deadline: datetime, submission_time: datetime,
                 has_valid_reason_ls=None, is_mc_ls_accepted=None,
                 has_valid_reason_ls_5d_yes=None, is_mc_ls_option_accepted=None,
                 has_valid_reason_ls_5d_no=None, is_mc_defer_accepted=None):
        self.name = name
        self.deadline = deadline
        self.submissionTime = submission_time

        self.has_valid_reason_ls = has_valid_reason_ls
        self.is_mc_ls_accepted = is_mc_ls_accepted

        self.has_valid_reason_ls_5d_yes = has_valid_reason_ls_5d_yes
        self.is_mc_ls_option_accepted = is_mc_ls_option_accepted

        self.is_mc_defer_accepted = is_mc_defer_accepted
        self.has_valid_reason_ls_5d_no = has_valid_reason_ls_5d_no

    def is_on_time(self) -> bool:
        """Shows if the cw was submitted on time"""
        submission_time = self.submissionTime
        deadline = self.deadline
        return submission_time < deadline

    def is_within_24_hours(self):
        """Shows if the cw was submitted within 24 hours """
        submission_time = self.submissionTime
        deadline = self.deadline
        interval: datetime = submission_time - deadline
        return interval <= timedelta(days=1)

    def is_within_5_days(self):
        """Shows if the cw was submitted within 5 days """
        submission_time = self.submissionTime
        deadline = self.deadline
        interval: datetime = submission_time - deadline
        return interval <= timedelta(days=5)

    def get_full_mark_category(self):
        """Tells the outcome according to the parameters"""

        # CW submitted on time
        if self.is_on_time():
            return self.FULL_MARK

        # CW submitted within 24 hours (late submission)
        if self.is_within_24_hours():
            # MC with a valid reason for late submission was accepted and CW gets Full Mark
            if self.has_valid_reason_ls and self.is_mc_ls_accepted:
                return self.FULL_MARK
            # MC was not accepted and CW gets 10 points less
            else:
                return self.DECREASED_MARK

        # CW submitted within 5 days
        if self.is_within_5_days():
            # CW has a valid reason for submitting in 5 days
            if self.has_valid_reason_ls_5d_yes:
                # MC is accepted
                if self.is_mc_ls_option_accepted:
                    # CW gets full mark
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
        """Displays mark message fully"""

        mark_category = self.get_full_mark_category()
        return self.marks[mark_category]


class Student:
    def __init__(self, name, id, group):
        self.id = id
        self.name = name
        self.group = group

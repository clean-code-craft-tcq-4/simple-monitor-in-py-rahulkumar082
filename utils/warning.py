from utils.language import Language
class Early_Warning(Language):
    def __init__(self, start=None, end=None) -> None:
        self.start = start
        self.end = end

    def check_early_limits(self, element_val, warning=True, language='English'):
        warning_tolerance = 0
        warning_tolerance = int(5 * 100 / self.end)
        unsafe_greater_limit = self.end - warning_tolerance
        if (compare_between(unsafe_greater_limit, element_val, self.end)):
            self.print_msg_in_language(language, "Warning: Approaching charge-peak", warning)
        unsafe_lower_limit = self.start + warning_tolerance
        if (compare_between(self.start, element_val, unsafe_lower_limit)):
            self.print_msg_in_language(language, "Warning: Approaching Discharge", warning)

def compare_between(start_val, middle, end_val):
    if (start_val <= middle <= end_val):
        return True
    return False
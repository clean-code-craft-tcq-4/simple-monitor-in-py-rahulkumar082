import operator

class Early_Warning:
    def __init__(self, start=None, end=None) -> None:
        self.start = start
        self.end = end
        self.warn_msg = lambda str, warning: print(f"{self.__class__.__name__}: {str}") if warning else None

    def check_early_limits(self, element_val, warning=True):
        warning_tolerance = 0
        warning_tolerance = int(5 * 100 / self.end)
        unsafe_greater_limit = self.end - warning_tolerance
        if (compare_between(unsafe_greater_limit, element_val, self.end)):
            self.warn_msg("Warning: Approaching charge-peak", warning)
        unsafe_lower_limit = self.start + warning_tolerance
        if (compare_between(self.start, element_val, unsafe_lower_limit)):
            self.warn_msg("Warning: Approaching Discharge", warning)

def compare_between(start_val, middle, end_val):
    if (start_val <= middle <= end_val):
        return True
    return False
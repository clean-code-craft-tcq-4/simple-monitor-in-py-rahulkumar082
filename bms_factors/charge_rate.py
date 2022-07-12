from utils.language import Language
from utils.range_checker import Range_Check
from utils.warning import Early_Warning


class Charge_Rate(Range_Check, Early_Warning, Language):
    def __init__(self) -> None:
        self.max_val = 0.8
        self.warn_msg = lambda str, warning: print(f"{self.__class__.__name__}: {str}") if warning else None
        super().__init__(end=self.max_val)

    def validate(self, coulumb_val, warning=True, language='English'):
        verbosity = True
        if (self.check_out_of_range(coulumb_val)):
            self.print_msg_in_language(language, "Charge rate is out of range!", verbosity)
            return False
        self.check_early_limits(coulumb_val, warning, language)
        return True

    def check_out_of_range(self, element_val):
        return (element_val > self.end)

    def check_early_limits(self, element_val, warning, language):
        end_val, element_val = tune_values(self.end, element_val)
        warning_tolerance = int(5 * 100 / end_val)
        unsafe_greater_limit = end_val - warning_tolerance
        if (unsafe_greater_limit <= element_val <= end_val):
            self.print_msg_in_language(language, "Warning: Approaching charge-peak", warning)

def tune_values(end_val, element_val):
    return (end_val*100, element_val*100)

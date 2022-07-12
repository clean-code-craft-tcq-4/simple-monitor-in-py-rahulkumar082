from utils.language import Language
from utils.range_checker import Range_Check
from utils.warning import Early_Warning


class State_Of_Charge(Range_Check, Early_Warning, Language):
    def __init__(self) -> None:
        self.min_req_percent = 20
        self.max_req_percent = 80
        Range_Check.__init__(self, start=self.min_req_percent, end=self.max_req_percent)
        Early_Warning.__init__(self, start=self.min_req_percent, end=self.max_req_percent)

    def validate(self, current_percentage, warning=True, language='English') -> bool:
        verbosity = True
        if(self.check_out_of_range(current_percentage)):
            self.print_msg_in_language(language, "State of Charge is out of range!", verbosity)
            return False
        self.check_early_limits(current_percentage, warning, language)
        return True

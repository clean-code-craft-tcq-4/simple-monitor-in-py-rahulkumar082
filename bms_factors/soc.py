from utils.range_checker import Range_Check
from utils.warning import Early_Warning


class State_Of_Charge(Range_Check, Early_Warning):
    def __init__(self) -> None:
        self.min_req_percent = 20
        self.max_req_percent = 80
        Range_Check.__init__(self, start=self.min_req_percent, end=self.max_req_percent)
        Early_Warning.__init__(self, start=self.min_req_percent, end=self.max_req_percent)
        print('Factor: ', self.__class__.__name__)

    def validate(self, current_percentage, warning=True) -> bool:
        verbosity = True
        if(self.check_out_of_range(current_percentage)):
            self.print_err_msg("State of Charge is out of range!", verbosity)
            return False
        self.check_early_limits(current_percentage, warning)
        return True

from utils.range_checker import Range_Check
from utils.warning import Early_Warning


class Temperature(Range_Check, Early_Warning):
    def __init__(self) -> None:
        self.start_c = 5
        self.end_c = 45
        Range_Check.__init__(self, start=self.start_c, end=self.end_c)
        Early_Warning.__init__(self, start=self.start_c, end=self.end_c)

    def validate(self, temperature_in_c, warning=True) -> bool:
        verbosity = True
        if (self.check_out_of_range(temperature_in_c)):
            self.print_err_msg("Temperature is out of range!", verbosity)
            return False
        self.check_early_limits(temperature_in_c, warning)
        return True

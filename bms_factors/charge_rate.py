from range_checker import Range_Check
class Charge_Rate(Range_Check):
    def __init__(self) -> None:
        self.max_val = 0.8
        super().__init__(end=self.max_val)

    def validate(self, coulumb_val, verbosity=False):
        if(self.check_out_of_range(coulumb_val)):
            self.print_msg("Charge rate is out of range!", verbosity)
            return False
        else:
            self.print_msg("Charge rate is in good range!", verbosity)
            return True
    def check_out_of_range(self, element_val):
        return (element_val > self.end)

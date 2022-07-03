from range_checker import Range_Check
class Charge_Rate(Range_Check):
    def __init__(self) -> None:
        self.max_val = 0.8
        self.min_val = 0.0
        super().__init__(start=self.min_val, end=self.max_val)

    def verify_charge_rate(self, coulumb_val, verbosity=False):
        if(self.check_out_of_range(coulumb_val)):
            self.print_msg("Charge rate is out of range!", verbosity)
            return False
        else:
            self.print_msg("Charge rate is in good range!", verbosity)
            return True

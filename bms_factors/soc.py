from range_checker import Range_Check
class State_Of_Charge(Range_Check):
    def __init__(self) -> None:
        self.min_req_percent = 20
        self.max_req_percent = 80
        super().__init__(start=self.min_req_percent, end=self.max_req_percent)

    def verify_soc_battery(self, current_percentage, verbosity=False) -> bool:
        if(self.check_out_of_range(current_percentage)):
            self.print_msg("State of Charge is out of range!", verbosity)
            return False
        else:
            self.print_msg("State of Charge is in good range!", verbosity)
            return True

class State_Of_Charge:
    def __init__(self) -> None:
        self.min_req_percent = 20
        self.max_req_percent = 80
        self.max_charge = 100
        self.min_charge = 0
        self.print_msg = lambda str, verbosity : print(str) if verbosity else None

    def verify_soc_battery(self, current_percentage, verbosity=False) -> bool:
        if(self.abnormal_value(current_percentage)):
            self.print_msg("Warning! The given current percentage does not apply, please re-check")
        elif(self.in_good_range(current_percentage)):
            self.print_msg("State of Charge is in good range!", verbosity)
            return True
        return False

    def abnormal_value(self, current_percentage) -> bool:
        if(current_percentage < 0 or current_percentage > 100):
            return True
        return False

    def in_good_range(self, current_percentage) -> bool:
        if current_percentage in range(self.min_req_percent, self.max_req_percent):
            return True
        return False
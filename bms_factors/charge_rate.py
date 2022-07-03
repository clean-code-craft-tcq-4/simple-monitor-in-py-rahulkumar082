class Charge_Rate:
    def __init__(self) -> None:
        self.max_val = 0.8
        self.min_val = 0.0
        self.print_msg = lambda str, verbosity : print(str) if verbosity else None
    
    def verify_charge_rate(self, coulumb_val, verbosity=False):
        if(self.abnormal_value(coulumb_val)):
            self.print_msg("Charge rate is out of range!", verbosity)
            return False
        elif(self.check_in_range(coulumb_val)):
            self.print_msg("Charge rate is in good range!", verbosity)
            return True

    def abnormal_value(self, coulumb_val) -> bool:
        if(coulumb_val < 0.0 or coulumb_val > 0.8):
            return True
        return False
    def check_in_range(self, coulumb_val) -> bool:
        if(coulumb_val >= 0.0 and coulumb_val <= 0.8):
            return True
        return False
            
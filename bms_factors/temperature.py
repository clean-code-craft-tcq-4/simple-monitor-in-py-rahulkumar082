from range_checker import Range_Check
class Temperature(Range_Check):
    def __init__(self) -> None:
        self.start_c = 5
        self.end_c = 45
        super().__init__(start=self.start_c, end=self.end_c)

    def verify_operating_temperature_with_battery(self, temperature_in_c, verbosity=False) -> bool:
        if(self.check_out_of_range(temperature_in_c)):
            self.print_msg("Temperature is out of range!", verbosity)
            return False
        else:
            self.print_msg("Temperature is good to charge!", verbosity)
            return True

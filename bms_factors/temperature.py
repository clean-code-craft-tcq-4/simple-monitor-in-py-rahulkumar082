class Temperature:
    def __init__(self) -> None:
        self.start_c = 5
        self.end_c = 45
        self.print_msg = lambda str, verbosity : print(str) if verbosity else None

    def verify_operating_temperature_with_battery(self, temperature_in_c, verbosity=False) -> bool:
        if(self.is_bad_temperature(temperature_in_c)):
            self.print_msg("Temperature is out of range!", verbosity)
            return False
        elif(self.is_ok_temperature(temperature_in_c)):
            self.print_msg("Temperature Okay to charge battery!", verbosity)
            return True

    def is_bad_temperature(self, temperature) -> bool:
        if(temperature < 5 or temperature > 45):
            return True
        return False

    def is_ok_temperature(self, temperature) -> bool:
        if(temperature in range(self.start_c, self.end_c+1)):
            return True
        return False

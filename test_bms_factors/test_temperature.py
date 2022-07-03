from bms_factors import temperature
class Testing_temperature:
    def __init__(self) -> None:
        self.test_obj = temperature.Temperature()
    def temperature_check(self):
        def test_all_ranges():
            for battery_temp in range(5, 46):
                assert(self.test_obj.verify_operating_temperature_with_battery(battery_temp, verbosity=False)) == True
            for battery_temp in range(-30, 5):
                assert(self.test_obj.verify_operating_temperature_with_battery(battery_temp, verbosity=True)) == False
            for battery_temp in range(50, 100):
                assert(self.test_obj.verify_operating_temperature_with_battery(battery_temp, verbosity=True)) == False
        test_all_ranges()
        print("All range tested well")
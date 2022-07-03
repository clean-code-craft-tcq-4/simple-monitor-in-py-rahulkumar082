from bms_factors import soc

class Testing_soc:
    def __init__(self) -> None:
        self.test_obj = soc.State_Of_Charge()
    
    def soc_check(self):
        def test_all_ranges():
            for battery_temp in range(0, 20):
                assert(self.test_obj.verify_soc_battery(battery_temp, verbosity=True)) == False
            for battery_temp in range(20, 80):
                assert(self.test_obj.verify_soc_battery(battery_temp, verbosity=True)) == True
            for battery_temp in range(80, 100):
                assert(self.test_obj.verify_soc_battery(battery_temp, verbosity=True)) == False
        test_all_ranges()
        print("All range tested well")
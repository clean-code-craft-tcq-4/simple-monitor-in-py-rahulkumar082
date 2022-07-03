from bms_factors import charge_rate

class Testing_soc:
    def __init__(self) -> None:
        self.test_obj = charge_rate.Charge_Rate()
        self.good_range = [x * 0.1 for x in range(0, 8)]
    
    def charge_rate_check(self):
        def test_all_ranges():
            for coulumb_val in range(-10, 0):
                assert(self.test_obj.verify_charge_rate(coulumb_val, verbosity=True)) == False
            for coulumb_val in self.good_range:
                assert(self.test_obj.verify_charge_rate(coulumb_val, verbosity=True)) == True
            for coulumb_val in range(1, 100):
                assert(self.test_obj.verify_charge_rate(coulumb_val, verbosity=True)) == False
        test_all_ranges()
        print("All range tested well")
from bms_factors import charge_rate, soc, temperature

class Check_Limits:
    def __init__(self) -> None:
        Temperature = temperature.Temperature()
        Charge_Rate = charge_rate.Charge_Rate()
        State_Of_Charge = soc.State_Of_Charge()
        self.dict_objs = {'temp_val': Temperature, 'soc_val': State_Of_Charge, 'cr_val': Charge_Rate}   

    def battery_is_ok(self, *args, verbosity=False):
        validate_conditions_arr = []
        obj_count = 0
        for key, obj in self.dict_objs.items():
            validate_conditions_arr.append(obj.validate(args[obj_count], verbosity))
            obj_count += 1
        return all(validate_conditions_arr)
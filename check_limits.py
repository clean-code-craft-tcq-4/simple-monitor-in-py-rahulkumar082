from bms_factors import charge_rate, soc, temperature

class Check_Limits:
    def __init__(self) -> None:
        self.obj_list = [
            temperature.Temperature(),
            soc.State_Of_Charge(),
            charge_rate.Charge_Rate()
        ]

    def battery_is_ok(self, arr_dict_obj, language='English'):
        validate_conditions_arr = []
        index = 0
        for dict_obj in arr_dict_obj:
            for val in dict_obj:
                warning = dict_obj.get(val, False)
                validate_conditions_arr.append(self.obj_list[index].validate(val, warning, language))
            index += 1
        return all(validate_conditions_arr)
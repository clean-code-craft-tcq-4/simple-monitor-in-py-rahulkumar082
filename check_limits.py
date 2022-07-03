from bms_factors import charge_rate, soc, temperature

Temperature = temperature.Temperature()
Charge_Rate = charge_rate.Charge_Rate()
State_Of_Charge = soc.State_Of_Charge()

def battery_is_ok(temperature_val, soc_val, charge_rate_val):
    is_temp_ok = Temperature.verify_operating_temperature_with_battery(temperature_val)
    is_soc_ok = State_Of_Charge.verify_soc_battery(soc_val)
    is_charge_rate_ok = Charge_Rate.verify_charge_rate(charge_rate_val)
    if(is_temp_ok and is_soc_ok and is_charge_rate_ok):
        return True
    else:
        return False

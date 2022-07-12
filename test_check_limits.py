from check_limits import Check_Limits

test_obj = Check_Limits()

if __name__ == '__main__':
    assert(test_obj.battery_is_ok([{25: True}, {70: True}, {0.76: True}], language='German') is True)
    assert(test_obj.battery_is_ok([{50: True}, {85: True}, {0: True}]) is False)
    assert(test_obj.battery_is_ok([{-1: True}, {21: True}, {0.8: True}]) is False)
    assert(test_obj.battery_is_ok([{6: True}, {19: True}, {0.8: True}]) is False)
    assert(test_obj.battery_is_ok([{6: True}, {20: True}, {0.9: True}]) is False)
    assert(test_obj.battery_is_ok([{30: True}, {70: True}, {0.5: True}]) is True)
    assert(test_obj.battery_is_ok([{30: True}, {78: True}, {0.5: True}]) is True)
    assert(test_obj.battery_is_ok([{30: True}, {78: True}, {0.5: True}]) is True)
    assert(test_obj.battery_is_ok([{30: True}, {78: True}, {0.5: True}]) is True)
    assert(test_obj.battery_is_ok([{25: True}, {35: True}, {0.5: True}]) is True)
    assert(test_obj.battery_is_ok([{25: True}, {70: True}, {0.76: True}]) is True)
    print("Tested!")

from check_limits import battery_is_ok

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7, verbosity=True) is True)
  assert(battery_is_ok(50, 85, 0, verbosity=True) is False)
  assert(battery_is_ok(-1, 21, 0.8, verbosity=True) is False)
  assert(battery_is_ok(6, 19, 0.8, verbosity=True) is False)
  assert(battery_is_ok(6, 20, 0.9, verbosity=True) is False)
  assert(battery_is_ok(30, 70, 0.5, verbosity=True) is True)
  print("Tested!")
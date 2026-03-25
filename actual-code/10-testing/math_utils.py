def add(a, b):
  # if a is not a int or float raise a typeerror
  if not isinstance(a, (int, float)):
    raise TypeError("a must be a int or float")
  if not isinstance(b, (int, float)):
    raise TypeError("b must be a int or float")
  return a + b

# something_test.py

# test_something.py
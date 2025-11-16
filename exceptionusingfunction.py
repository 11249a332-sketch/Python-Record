def divide(x, y):
  try:
      result = x / y
  except ZeroDivisionError:
      print "division by zero!"
  else:
      print "result is", result
  finally:
      print
      "executing finally clause"

  divide(12, 0)
  divide("12", "2")  # No 'TypeError' exception caught in this case.

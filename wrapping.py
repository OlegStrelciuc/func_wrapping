def wrap_brackets( text ):
  return "(" + text + ")"


def wrap_square_brackets( text ):
  return "[[[" + text + "]]]"


def wrap_signs( text ):
  return "<<<" + text + ">>>"


print(wrap_signs(wrap_square_brackets(wrap_brackets("12345"))))


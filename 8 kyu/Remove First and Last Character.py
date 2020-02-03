def remove_char(s):
  a = list(s)
  a.pop(0)
  a.pop(-1)
  return "".join(a)
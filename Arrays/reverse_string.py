def reverse_string(s: str):

  if not isinstance(s, str):
    raise TypeError

  s1 = []

  for i in range(len(s)):
    s1.append(s[len(s) - 1 - i])

  return s1


s = 'hello how are you'
print(reverse_string(s))

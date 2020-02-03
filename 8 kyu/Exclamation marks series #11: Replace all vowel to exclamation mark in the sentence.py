def replace_exclamation(s):
    for letter in s:
       if letter in 'aeiouAEIOU':
           s = s.replace(letter,'!')
    return s
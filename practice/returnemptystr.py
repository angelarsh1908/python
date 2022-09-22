def string_both_ends(str):
   if len(str) < 2:
    return ''
   return str[0:2] + str[-2:]

a=(string_both_ends('w3resource'))
print(a)
print(string_both_ends('w3'))
print(string_both_ends('tyyyyyyyyyyyyyyyyy'))
    

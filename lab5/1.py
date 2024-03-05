import re 
s = input()
if re.findall("ab*", s):
    print(True)
else:
    print(False)
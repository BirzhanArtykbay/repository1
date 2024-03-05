import re
s = input()
result = re.findall("[A-Z][^A-Z]*", s)
print(result)
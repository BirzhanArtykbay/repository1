import re
s = input()
words = s.split("_")
result = words[0] + "".join(i.capitalize() for i in words[1:])
print(result)
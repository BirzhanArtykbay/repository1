import re
s = input()
result = re.search("a.*b$", s)
print(result)
import re
s = input()
result = re.sub(r"(\w)([A-Z])", r"\1 \2", s)
print(result)
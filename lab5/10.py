import re
s = input()
words = re.findall(r"[A-Z]*[a-z]+", s)
result = "_".join(i.lower() for i in words)
print(result)
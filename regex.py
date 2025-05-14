import re

### float digit
t = int(input())
for _ in range(t):
    n = input()
    print(False if re.match(r'^[+-]?(\d+\.\d+|\.\d+)$', n) is None else True)

### split
regex_pattern = r"[,.]"
print("\n".join(re.split(regex_pattern, input())))

### key group
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
m.groupdict()
# {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}

### match toutes les suites de characters alphanumeric
s = "..12345678910111213141516171820212223" # [1, 2]
s2 = "__init__" # []
s3 = "__comma__" # ['m']
m = re.findall(r'([a-zA-Z0-9])\1{1,}', s)
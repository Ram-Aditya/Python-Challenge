#Challenge URL = "http://www.pythonchallenge.com/pc/def/equality.html

import re
matches = []

fp = open("Challenge3text.txt", "r")

for line in fp:
    matches += (re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', line))

result = ""
for i in matches:
    result += i[4]
print(result)
fp.close()
#Challenge URL "http://www.pythonchallenge.com/pc/def/ocr.html"

storage = {}

f = open("Challenge2text", "r")

for line in f:
    for i in line:
        x = i
        if x in storage:
            storage[x] += 1
        else:
            storage[x] = 1


result = ''.join(list(filter(lambda x:(storage[x] == 1), storage)))
f.close()
print(result)
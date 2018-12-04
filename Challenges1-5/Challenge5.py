#Challenge URL = "http://www.pythonchallenge.com/pc/def/peak.html"

import pickle, urllib.request


page = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

result = pickle.load(page)

#print(result)

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j][0] * result[i][j][1], end ="")
    print()
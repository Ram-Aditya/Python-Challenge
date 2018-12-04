#Challenge URL = "http://www.pythonchallenge.com/pc/def/linkedlist.html"x`
import requests
import re

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url_list = [12345]
url = base_url + "12345"

for i in range(400):
    response = requests.get(url)
    print(response.text)
    next_url_val = re.search(r'[0-9]{3,5}', str(re.search(r'nothing is [0-9]{3,5}', response.text).group())).group()
    url_list.append(next_url_val)
    url = base_url + str(next_url_val)


#print(url_list)

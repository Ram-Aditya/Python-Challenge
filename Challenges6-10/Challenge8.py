#Challenge URL = "http://www.pythonchallenge.com/pc/def/integrity.html"

#Go to the page source and get the username and password from the comments
import bz2
# import requests
#import selenium
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'


username = bz2.decompress(un).decode('utf-8')
password = bz2.decompress(pw).decode('utf-8')

print(username, password)

# result_page_url = "http://" + str(username) + ":" +  str(password) + "@www.pythonchallenge.com/pc/return/good.html"
#
# result_page = requests.get(result_page_url)
# print(result_page.text)
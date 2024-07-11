import requests,sys
from fake_useragent import UserAgent
ua = UserAgent()

#time.sleep(random.randint(5,60))

url = "https://xn--80aaahf3a6anlhog.xn--p1ai/inap/likes"
payload = {"path":"participants","id":sys.argv[1]}


print(requests.post(url,headers={"User-Agent":ua.random},json=payload).text)

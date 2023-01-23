from pydoc import source_synopsis
import requests
from bs4 import BeautifulSoup
import lxml.html as LH

r = requests.get("https://www.shodan.io/search?query=SSH")
soup = BeautifulSoup(r.text, "html.parser")
dom = LH.fromstring(r.text)
i = 3
print(r.text)
for _ in range(0,10):
    ip = []
    ips = dom.xpath("/html/body/div[3]/div/div[2]/div["+str(i)+"]/div[2]/a")
    for k in ips :
        file = open("ip.txt", "a")
        file.write(k.text)
        file.write('\n')
        file.close()
    i = i + 1
for i in ip:
    print(i)
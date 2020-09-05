import requests
from lxml import etree
import json

f= open('data.csv', 'r', encoding='utf-8')
data = json.loads(f.read())

head = {'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

for i in data:
    response = requests.get(url=i,headers=head).text
    tree = etree.HTML(response)
    datas =tree.xpath('//div[@class="item-description"]/div')
    for d in datas:
        if len(d)<1:continue
        url = d.xpath("./a/@href")
        title = d.xpath('./text()')
        dic =  {
            '标题':title[0],
            '链接':url[0]
        }
        print(dic)
        with open('../text.txt', 'a', encoding='utf-8')as fp:
            fp.write(title[0] + '\r' + url[0] + '\r\n')



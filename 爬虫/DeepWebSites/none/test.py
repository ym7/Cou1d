from lxml import etree

f= open('test.html', 'r', encoding='utf-8')
data = f.read()

tree = etree.HTML(data)
import json
datas =tree.xpath('//div[@class="item-description"]/div')
for d in datas:
    if len(d)<1:continue
    url = d.xpath("./a/@href")
    title = d.xpath('./text()')
    with open('../text.txt', 'a', encoding='utf-8')as fp:
        fp.write(title[0]+'\r'+url[0]+'\r\n')


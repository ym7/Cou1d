import requests
from lxml import etree
import os
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

url = 'https://www.moer.cn/'

def getthis():
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="feedList"]/li')
    # print(li_list)
    data = []
    for li in li_list:
        title = li.xpath('.//a/text()')[0]
        zhaiyao = li.xpath('./div[1]/p/span/text()')
        author = li.xpath('./div[2]/div[1]/a[2]/text() | ./div[2]/div[1]/a[1]/text()')
        detial_url = li.xpath('./div[1]/a/@href')
        fp=open('摩尔金融数据.json','w')
        for one_url in  detial_url:
            # print('正在采集'+one_url)
            #获取文章ID
            article_id = int(str(one_url).split('=')[-1])
            #浏览量是动态数据
            watched_url = f'https://www.moer.cn/articleCountAndStatus.json?articleId={article_id}'
            watched = requests.get(url=watched_url, headers=headers).json()
            watched_count = watched['result']['authorArticle_browseCount']
            #详情页页面
            detail_page_text = requests.get(url=one_url,headers=headers).text
            one_tree = etree.HTML(detail_page_text)
            #发布时间
            send_time = one_tree.xpath('/html/body/div[1]/div[1]/article/section[1]/p/span[1]/text()')
            #评论数量
            issuce = one_tree.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/ul/li[2]/a/text()')
            #点赞数量
            dianzan = one_tree.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/a/b/text()')
            #构造字典数据结构
            dic2 = {
                '标题':title.rsplit('\n')[0],
                '摘要': zhaiyao[0],
                '作者': author[0],
                '浏览量': str(watched_count),
                 }
            #每循环一次，向字典中添加dic2
            data.append(dic2)
            import json
            # fileobj = json.dumps(data,ensure_ascii=False)
            # fp.write(fileobj)
            # print(dic2,'\n'+'采集成功')
            new_data = json.dumps(data)
            return new_data



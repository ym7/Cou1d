import requests
import selenium
from lxml import etree


def page_text():
    url = 'https://bj.58.com/ershoufang/'
    vars  = {'cookie': "f=n; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; time_create=1601519655220; userid360_xml=7A5E640C7BF1CF0D9DCF3DA90FE72A8A; myLat=""; myLon=""; id58=3YTYMF9NsxXle1UKBjmJfA==; spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT; mcity=qj; 58tj_uuid=bcd6f0bb-76da-42a7-8ecf-0f77af55d3e1; new_uv=1; utm_source=market; init_refer=https%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc.K00000jSRdBEvgGGi71aXtI_8gZwHxdsLqlOqn-XbGlKKoT3BkTsVPTvFrvQoiy4GUIrDrUW7EMO80O7ZCN4hhvBg_rw1R5WwNqQLXUeVFkzVKmVeF5SdJzCIuNC7WmhIyAD2trZwwoL_Bp09FY37SNxQVAv2iUlS7PNbsmL7k3B6n1Diq0kGXgfOoNvsTkdwM1eTsaWx0Fx9onfDVaTpMLbHgFj.DY_NR2Ar5Od66z3PrrW6ButVvkDj3n-vHwYxw_vU85YIMAQV8qhORGyAp7WIu8L6.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqPHWPoQ5Z0ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5HR31pz1ksKzmLmqnfKdThkxpyfqnHRkrHDvrjRYPsKVINqGujYknWTknHbdP0KVgv-b5HDsPWTLPHbd0AdYTAkxpyfqnHDdn1f0TZuxpyfqn0KGuAnqiD4a0APzm1Ydnjb1rf%2526ck%253D5663.1.61.377.160.377.151.385%2526dt%253D1598927626; als=0; wmda_uuid=23c39d8394ff0bf69b8b3ae98b7382a4; wmda_new_uuid=1; wmda_session_id_11187958619315=1598927641541-35c6d3e4-ca01-9a10; new_session=0; f=n; city=bj; 58home=bj; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; commontopbar_ipcity=qj%7C%E6%9B%B2%E9%9D%96%7C0; JSESSIONID=48FDFBBA86780B4D393244DB38A71A25; wmda_session_id_6333604277682=1598927652308-e46932fe-c51c-b930; wmda_visited_projects=%3B11187958619315%3B6333604277682; xzfzqtoken=hPbo1K32d%2FiPPhAkEhwWKQU9BaeEWo4nQzdQQttQPpWNrxxHsg%2FpPPKw8v%2Fq7iDyin35brBb%2F%2FeSODvMgkQULA%3D%3D; xxzl_deviceid=Esfjav%2Bh6JIgY00Qc80iEoFe3KBSbeaKpdSxEGfVuHnh0e9NhrII62JLRgD8Nftl"}
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    response = requests.get(url=url,headers=headers,params=vars).text
    return response

def page_parser():
    data = []
    res = page_text()
    tree = etree.HTML(res)
    ul_list = tree.xpath('/html/body/div[5]/div[5]/div[1]/ul/li')
    for li in ul_list:
        title = li.xpath('.//div[@class="list-info"]/h2/a/text()')[0]
        content = li.xpath('./div[2]/p[1]/text()')[0]
        company = li.xpath('./div[2]/div/span[1]/text()')[0]
        money = li.xpath('./div[3]/p[1]/b/text()')[0] +'万'
        unit = li.xpath('./div[3]/p[2]/text()')[0]
        dic = {
            '标题':title.strip(),
            '房型':content.strip(),
            '所属公司':company.strip(),
            '价格':money.strip(),
            '价值':unit.strip()
        }
        data.append(dic)
    return data

def saving():
    import pymysql
    conn = pymysql.Connect(host='')
    cur = conn.cursor()



if __name__ == '__main__':
    page_parser()

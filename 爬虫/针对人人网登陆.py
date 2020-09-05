# 编码流程：
# 1.验证码识别，获取验证码图片的文字数据
# 2。对post请求进行发送(处理请求参数)
# 3.对响应数据进行持久化存储

import requests
from lxml import etree

from codeClass import YDMHttp

# 1.对验证码图片进行捕获和识别

if __name__ == '__main__':
    url = 'http://www.renren.com/SysHome.do'
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    session = requests.Session()
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
    code_img_data = requests.get(url=code_img_src, headers=headers).content
    with open('code.jpg', 'wb')as fp:
        fp.write(code_img_data)


    # 使用云打码提供的示例代码对验证码图片进行识别
    def getCodeText(imgPath, codeType):
        username = 'ym786337077'
        # 密码
        password = 'ym786337077'
        # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
        appid = 8633
        # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
        appkey = '1dce807a0a6f95a75f60b33c5ca10580'
        # 图片文件
        filename = imgPath
        # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
        codetype = codeType
        # 超时时间，秒
        timeout = 20
        result = None
        # 检查
        if (username == 'username'):
            print('请设置好相关参数再测试')
        else:
            # 初始化
            yundama = YDMHttp(username, password, appid, appkey)

            # 登陆云打码
            uid = yundama.login();
            print('uid: %s' % uid)

            # 查询余额
            balance = yundama.balance();
            print('balance: %s' % balance)

            # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
            cid, result = yundama.decode(filename, codetype, timeout);
            print('cid: %s, result: %s' % (cid, result))

        return result


    result = getCodeText('code.jpg', 1000)

    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201976958488'
    data = {
        'email': '18687433229',
        'icode': result,
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': 'xx',
        'rkey': '331da058ee000ef0cf4dd890b048d3c9',
        'f': 'http%3A%2F%2Fwww.renren.com%2F971946892%2Fnewsfeed%2Fphoto'
    }

    login_page_text = session.post(url=login_url, headers=headers, data=data).text
    pro_url = 'http://www.renren.com/971946892/profile'
    page_text = session.get(url=pro_url,headers=headers).text
    with open('renren.html', 'w', encoding='utf-8')as fp:
        fp.write(page_text)

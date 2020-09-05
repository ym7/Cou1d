from aip import AipSpeech, AipNlp
import time
import os

""" 你的 APPID AK SK """
APP_ID = '18826103'
API_KEY = 'FrggildY0qBXHo2HdDWCxPLL'
SECRET_KEY = 'xnjbyGTuTjAGlEbO10D1yqtDlVbzCa6r'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
nlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    if not filePath:
        os.system(f"ffmpeg -y  -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
        with open(f"{filePath}.pcm", 'rb') as fp:
            return fp.read()
    else:
        with open(f"{filePath}", 'rb') as fp:
            return fp.read()


def text2audio(text):
    # 合成配置
    filename = f"{time.time()}.mp3"
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
        'spd': 3,
        'pit': 7,
        'per': 4
    })
    # 生成文件
    if not isinstance(result, dict):
        with open(filename, 'wb') as f:
            f.write(result)
    return os.system(filename)


def audio2text(filePath):
    # 识别文件
    res = client.asr(get_file_content(filePath=filePath), 'pcm', 16000, {
        'dev_pid': 1537,
    })

    '''
    1537	普通话(纯中文识别)	输入法模型	有标点	支持自定义词库
    1737	英语		无标点	不支持自定义词库
    1637	粤语		有标点	不支持自定义词库
    1837	四川话		有标点	不支持自定义词库
    1936	普通话远场	远场模型	有标点	不支持
    '''
    print(res['result'][0])
    return res.get("result")[0]


def to_tuling(text):
    import requests

    args = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": text
            }
        },
        "userInfo": {
            "apiKey": "9a9a026e2eb64ed6b006ad99d27f6b9e",
            "userId": "1111"
        }
    }

    url = "http://openapi.tuling123.com/openapi/api/v2"

    res = requests.post(url, json=args)

    text = res.json().get("results")[0].get("values").get("text")
    return text


# res = nlp.simnet("你叫什么名字","你的名字是什么")
# print(res)


# try:
#     text = audio2text("./static/pcm/321go.pcm")
#     filename = text2audio(text)
#
#     os.system(filename)
# except Exception as e:
#     print("Errors")

if __name__ == '__main__':
    audio2text("./static/pcm/321go.pcm")
    res = text2audio("今天天气不错")
    os.system(res)

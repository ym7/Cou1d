from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '18826103'
API_KEY = 'FrggildY0qBXHo2HdDWCxPLL'
SECRET_KEY = 'xnjbyGTuTjAGlEbO10D1yqtDlVbzCa6r'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


#读取文件
def get_file_content(filePath):
    with open(filePath,'rb')as fp:
        return fp.read()
#识别文件
res = client.asr(get_file_content('./static/pcm/background1.pcm'),'pcm',16000,{
    'dev_pid':1537,
})

'''
1537	普通话(纯中文识别)	输入法模型	有标点	支持自定义词库
1737	英语		无标点	不支持自定义词库
1637	粤语		有标点	不支持自定义词库
1837	四川话		有标点	不支持自定义词库
1936	普通话远场	远场模型	有标点	不支持
'''
print(res['result'])
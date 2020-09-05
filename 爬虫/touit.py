from ctypes import windll
import win32api
import win32con
import time



def mouse_eve(x,y):
    windll.user32.SetCursorPos(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)

def back_eve():
    windll.user32.SetCursorPos(1350, 90)
    mouse_eve(1350, 90)

def whell_eve(arg):
    for i in range(arg):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1)

timeing = lambda x :time.sleep(x)

mouse_eve(1600,400)
whell_eve(2000)
timeing(0.5)
mouse_eve(1350,750)
#返回时间
timeing(6)
back_eve()

i = 1
while i >0:
    mouse_eve()
    i-=1



# windll.user32.SetCursorPos(1350,850)
# mouse_eve(1350,850)

# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,1350,90)
# time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,1350,90)

# import requests
# headers = {
#     "X - Requested - With": "XMLHttpRequest",
#     "access_token": "ylxf_api_v1.0",
#     "Content - Type":" application / x - www - form - urlencoded",
#     "Accept": "application / json",
#     "User - Agent": "Mozilla / 5.0(Linux;Android5.1.1;MI9Build / NMF26X;wv) AppleWebKit / 537.36(KHTML, likeGecko) Version / 4.0Chrome / 74.0.3729.136MobileSafari / 537.36ylxfAppHtml5Plus / 1.0",
#     "App_version":" 1.1.18",
#     "Authorization": "811D49B20A874CAED57C569033597ED00B6023FC9300C6919BA0FD954585B0B6EBF4C3C00AB6EB804CBA34DD124A0F20EB73DCD56B48BF7F3A805DEF94759371F515C9354EEEBF18439FAAAE37F5B6B61CDA5920AB0BC0E0D73B5848B8997A4399B0A2BC11FB99798A603AEFDADE6813487B1994B15EDCB5ABCA952BECF26C89A5657D712F6FDE92",
#     "Host":" ms.ylxf.1237125.cn",
#     "Connection": "Keep - Alive",
#     "Accept - Encoding": "gzip",
#     "Content - Length": 70,
#     "userId":3517144769866235911,
#     "chapterId":1026554310345412608,
#     "timeout":60000
# }
# json = {
#     'IsFinished':1
# }


# res = requests.post(verify=False,url='https://ms.ylxf.1237125.cn/app/apiv1/ylxf/course/chapter/detail',data=headers,json=json)
# print(res.text)


# import sys
# import os
# import re
# import time
# from com.dtmilano.android.viewclient import ViewClient
#
#
#
# def test():
#     # 连接手机
#     device, serialno = ViewClient.connectToDeviceOrExit()
#     vc = ViewClient(device, serialno)
#     # 按HOME键
#     device.press('KEYCODE_HOME')
#     time.sleep(3)
#     # 找到微信图标
#     vc.dump()
#     weixin_button = vc.findViewWithTextOrRaise(u'微信')
#     # 点击微信图标
#     weixin_button.touch()
#     time.sleep(10)
#     # 找到第一个联系人/群
#     # 可以使用UI Automator Viewer查看到对应第一个联系人/群的resource-id为"com.tencent.mm:id/auj"
#     vc.dump()
#     group_button = vc.findViewByIdOrRaise("com.tencent.mm:id/auj")
#     # 点击进群
#     group_button.touch()
#     time.sleep(5)
#     # 找到输入框并输入当前时间
#     vc.dump()
#     vc.findViewByIdOrRaise("com.tencent.mm:id/aep").setText('Now:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
#     time.sleep(3)
#     # 点击发送按钮
#     vc.dump()
#     vc.findViewWithTextOrRaise(u'发送').touch()
#
#
# if __name__ == '__main__':
#     test()
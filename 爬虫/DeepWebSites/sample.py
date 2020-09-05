with open('./text.txt','r',encoding='utf-8')as fp:
    data = fp.read()

par ="http.*/"

import re
url_list  = re.findall(par,data)
import json




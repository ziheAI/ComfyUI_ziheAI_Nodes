#@CopyRight By 子禾AI【ziheAI.com】
#严禁在未经授权情况下用于任何商用行为
#🔧 **定制开发服务**  
#- 企业级AI工作流开发  
#- 私有化节点定制  
#- 性能优化服务 
#- 联系微信ziheAI567   

#📧 商务合作：ziheAI567@163.com

import http.client
import hashlib
import urllib.parse
import urllib.request
import random
import json
import requests
import os
import re
from ..base.base_node import BaseNode

# 读取json
configs_dir = os.path.join(os.path.dirname(__file__), '..', 'configs')
json_file = os.path.join(configs_dir, 'BaiduApikey.json')

# 检查目录是否存在，不存在则创建
if not os.path.exists(configs_dir):
    os.makedirs(configs_dir)

# 检查配置文件是否存在，不存在则创建
if not os.path.exists(json_file):
    default_config = {
        "baidu_dev_appid": "", 
        "baidu_dev_appkey": ""
    }
    with open(json_file, 'w') as f:
        json.dump(default_config, f, indent=4)
    api_dict = default_config
    print(f"## ✉️ziheAI Nodes: 配置文件不存在，已创建默认配置: {json_file}")
else:
    with open(json_file, 'r') as f:
        api_dict = json.load(f)

# 判断字符串是否包含中文
def is_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

# 替换字符串中间一部分为'*'，reserve_digits是首尾保留位数
def string_asterisk_mask(str_, reserve_digits):
    if len(str_)==1:
        return '*'
    elif len(str_) <= reserve_digits * 2:
        return str_[:1] + re.sub(r'.','*', str_[1:])
    else:
        return (str_[:reserve_digits]
                + re.sub(r'.','*', str_[reserve_digits:-reserve_digits])
                + str_[-reserve_digits:])


# 通用翻译模块
class BaiduTranslate_API(BaseNode):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        Channel = [
            'Free', 'API',
        ]
        return {
            'required': {
                'text': ('STRING', {'multiline': True}),
                "Channel": (Channel,),
                'Translate_To': (['en', 'zh'], {'default': 'en'}),   
            },
        }

    RETURN_TYPES = ('STRING',)
    FUNCTION = 'BaiduTranslate_API'

    def BaiduTranslate_API(self, text, Translate_To, Channel):

        # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
        from_lang = 'auto'
        to_lang = Translate_To
        translate_result = ''
        debugmsg = ''

        if Channel == 'API':
            # get appid and appkey
            appid = api_dict['baidu_dev_appid']
            appkey = api_dict['baidu_dev_appkey']
            url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
            query = text

            print(f'## ✉️ziheAI Nodes: API文本翻译, appid={string_asterisk_mask(appid, 3)}, '
                  f'appkey={string_asterisk_mask(appkey, 3)}, url={url}')

            # Generate salt and sign
            salt = random.randint(32768, 65536)
            s = appid + query + str(salt) + appkey
            sign = hashlib.md5(s.encode('utf-8')).hexdigest()

            # Build request
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

            result = [{'src': '', 'dst': 'error!'}]
            try:
                response = requests.post(url, params=payload, headers=headers).json()
                debugmsg = str(response)
                if "trans_result" in response:
                    result = response['trans_result']

            except Exception as e:
                print(e)

            for line in result:
                translate_result = translate_result + (line['dst']) + '\n'
            translate_result = translate_result[:-1]
            print('## ✉️ziheAI Nodes: API文本翻译: ' + text + ' ===》 ' + translate_result)
            if translate_result == 'error!':
                print(debugmsg)

        if Channel == 'Free':
            # 读取百度翻译的加盐算法
            import execjs
            js_dir = os.path.join(os.path.dirname(__file__), '..', 'js')
            js_file = os.path.join(js_dir, 'BaiduTranslate_Free.js')
            with open(js_file, 'r', encoding='utf-8') as f:
                sign_js = execjs.compile(f.read())

            token = '012cd082bf1f821bb7d94981bf6d477a'
            url = 'https://fanyi.baidu.com/v2transapi'
            print(f'## ✉️ziheAI Nodes: Free文本翻译, token={string_asterisk_mask(token, 3)}, url={url}')
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'cookie': 'BIDUPSID=3641572D5E0DB57A2F20F8F3373E302C; PSTM=1687090179; '
                          'BAIDUID=3641572D5E0DB57AF59F1D83EEBC5D2B:FG=1; BAIDUID_BFESS=3641572D5E0DB57AF59F1D83EEBC5D2B:FG=1; '
                          'ZFY=sGU1ho9nxRf2CX2bcYMVcfSXr9y2:BmKBeBdv7CDGhUs:C; '
                          'BDUSS'
                          '=tXaEJQVkxBeVBHMllBWWh1aTVZLXlhcVVqTWNCOXJGfmwzUUJmaHphWm1zZGRrSVFBQUFBJCQAAAAAAAAAAAEAAADWpvEyzqiwrsTjtcTQocPXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGYksGRmJLBkam; BDUSS_BFESS=tXaEJQVkxBeVBHMllBWWh1aTVZLXlhcVVqTWNCOXJGfmwzUUJmaHphWm1zZGRrSVFBQUFBJCQAAAAAAAAAAAEAAADWpvEyzqiwrsTjtcTQocPXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGYksGRmJLBkam; newlogin=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=00aka5a12g80a10g25a52l0g1ie1gm11p; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; delPer=0; H_PS_PSSID=36550_39112_39226_39222_39097_39039_39198_39207_26350_39138_39225_39094_39137_39101; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1692451747; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1692451747; ab_sr=1.0.1_ZmQ3OWYzODRjZGNkOTYxOWI4ZTVhYjRmNTAwNjYyYTUwYmI3OGY2NTViMzhkNWYzM2IxZTVhNjAwNjdkMTU0ODE4Yzc2YmI3OGRmNTY3Y2QxMzZiZDRmZDIwMGIwYmQ2NGI5M2QzZWFlNmNkODBhZjllZDcxNGFkMTEyNmY0NGNhZGZjMTlmOGQ2YjIxNzNhMmUxNDJkMDhlZTM1NjhiZjkyMDc2MmQxN2Q5ODg3NDBkZGViNTEzMDU2NDQzNGEy'}

            sign = sign_js.call('e', text)
            data = {'from': from_lang,
                    'to': to_lang,
                    'query': text,
                    'transtype': 'realtime',
                    'simple_means_flag': 3,
                    'sign': sign,
                    'domain': 'common',
                    'token': token}

            result = [{'src': '', 'dst': 'error!'}]
            try:
                response = requests.post(url, headers=headers, data=data).json()
                debugmsg = str(response)
                if "trans_result" in response:
                    result = response['trans_result']['data']

            except Exception as e:
                print(e)

            for line in result:
                translate_result = translate_result + (line['dst']) + '\n'
            translate_result = translate_result[:-1]
            print('## ✉️ziheAI Nodes: Free文本翻译: ' + text + ' ===》 ' + translate_result)
            if translate_result == 'error!' :
                print(debugmsg)
        return (translate_result,)
"""接口封装的基础类-完成GET、POST请求封装以及登录授权等"""
import requests


class BaseApi:
    def __init__(self,base_url=None):
        self.base_url = base_url
        self.session = requests.Session()


    def login(self, user, password):
        url = self.base_url+'/admin/privilege.php'
        payload = {
            'username': user,
            'password': password,
            'act': 'signin'
        }

        # session 可以保持回话 (自动保存cookies)
        self.session.post(url, data=payload)
        return self

    def get(self, url, *args, **kwargs):
        # 如何url没有已http 开头，视为接口路劲，拼接上当前服务地址
        if isinstance(url,str) and not url.startswith('http'):
            url = self.base_url+url
        return self.session.get(url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        if isinstance(url,str) and not url.startswith('http'):
            url = self.base_url+url
        return self.session.post(url, *args, **kwargs)


if __name__ == '__main__':
    api = BaseApi(base_url='https://newecshop.longtest.cn')
    api.login('test02','test02')
    url = '/admin/category.php?is_ajax=1'
    data = {
        "act": 'query',
        "cat_name": "电脑",
        "page": '1'
    }
    res = api.post(url, data=data)
    print(res.text)




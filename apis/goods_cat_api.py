from apis.base_api import BaseApi


class GoodsCatApi(BaseApi):
    """查询商品分类"""
    def get_goods_cat(self, cat_name, page=1):
        url = '/admin/category.php?is_ajax=1'
        data = {
            "act": 'query',
            "cat_name": cat_name,
            "page": page
        }
        res = self.post(url, data=data)
        return res

"""测试商品分类"""
import pytest

from utils.data_file_utils import load_csv
from utils.path_utils import data_dir


def test_get_goods_caat(goods_cat):
    res = goods_cat.get_goods_cat('电脑')
    print(res.text)
    assert res.json()['error'] == 0, '响应中的error应为0'


# cvs文件批量查询数据
def test_get_goods_cat_with_csv(goods_cat):
    data = load_csv('D:/api-pythonproject/data/goods_cat.csv')
    for _goods_cat, page in data:
        print(_goods_cat, page)
        res = goods_cat.get_goods_cat(_goods_cat, page)
        # print(res.text)
        assert res.json()['error'] == 0, '响应中的error应为0'


@pytest.fixture
def item():
    data = load_csv('D:/api-pythonproject/data/goods_cat.csv')
    for item in data:
        yield item


# ddt 数据工厂
# data = load_csv(data_dir / 'goods_cat.csv')
@pytest.mark.parametrize('item', load_csv(data_dir / 'goods_cat.csv'))
def test_get_goods_cat_with_ddt(goods_cat,item):
        res = goods_cat.get_goods_cat(*item)
        # print(res.text)
        assert res.json()['error'] == 0, '响应中的error应为0'

def test_a():
    pass

def test_b():
    pass

def test_c():
    pass
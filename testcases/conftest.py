import pytest

from apis.base_api import BaseApi
from apis.goods_cat_api import GoodsCatApi


@pytest.fixture
def api(user, base_url):
    return BaseApi(base_url).login(*user)
    # base_api = BaseApi()
    # username, password = user
    # base_api.login(user, password)


@pytest.fixture
def goods_cat(user, base_url):
    return GoodsCatApi(base_url).login(*user)

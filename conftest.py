import os
import platform

import pytest
from datetime import datetime

from apis.base_api import BaseApi
from utils.db_utils import MySQLUtils

NOW = datetime.now()  # 当前时间


# 获取数据库配置 不用pytest ini 插件
# def pytest_addoption(parser: pytest.Parser):
#     parser.addini('db_host', help='数据库服务地址')
#     parser.addini('db_port', help='数据库端口号')
#     parser.addini('db_user', help='链接数据库账号')
#     parser.addini('db_password', help='链接数据库密码')
#     parser.addini('db_name', help='数据库名称')


def pytest_configure(config: pytest.Config):
    """ 用于修改pytest配置 """
    # config.get_option()  # 获取pytest执行命令行参数
    # 获取原来的pytest.ini中的log_file配置
    log_file = config.getini('log_file')  # 过去pytest.ini中的配置
    root_dir = config.rootpath  # 获取项目的跟目录
    if log_file is not None:
        # 项目跟目录，连接 配置的路径(并使用当前日期时间进行格式化) 并修改原有的log_file参数
        config.option.log_file = root_dir / NOW.strftime(log_file)

    # 处理allure报告路径
    alluredir = config.getoption('--alluredir')
    if alluredir is not None:
        config.option.allure_report_dir = root_dir / alluredir


# # 不用pytest.ini库进行文件查找
# from configparser import ConfigParser
# def pytest_addoption(parser:pytest.Parser):
#     parser.addini('env',help='制定环境')
#
# @pytest.fixture
# def env_vars(request):
#     config_file = request.config.rootpath / 'pytest.ini'
#     conf = ConfigParser()
#     conf.read(config_file)
#
#     env = request.config.getini('env')
#     if conf.has_section(env):
#         return dict(conf.items(env))


# 定制流程
# def pytest_terminal_summary(terminalreporter, exitstatus, config: pytest.Config):
#     """运行后的命令行总结"""
#     if config.getoption('--alluredir') is not None:
#         if 'Windows' in platform.platform():
#             alluer = config.rootpath / 'tools/allure-2.18.0/bin/allure.bat'
#         else:
#             alluer = config.rootpath / 'tools/allure-2.18.0/bin/allure'
#
#         alluer_date = config.option.allure_report_dir
#         alluer_html = config.rootpath / 'reports/allure-html'
#         os.system('%s generate  %s -o %s' % (alluer, alluer_date, alluer_html))
#         print('alluer htm报告生成成功')


@pytest.fixture
def base_url(env_vars):
    """ 返回基本url配置 """
    return env_vars.get('base_url')


@pytest.fixture
def user(env_vars):
    """ 返回用户姓名和密码配置 """
    return env_vars.get('user'), env_vars.get('password')


@pytest.fixture
def Db(env_vars):  # need pip install pytest-ini
    host = env_vars.get('db_host')
    port = env_vars.get('db_port')
    user = env_vars.get('db_user')
    password = str(env_vars.get('db_password'))
    db = env_vars.get('db_name')
    return MySQLUtils(host, port, user, password, db)

    # return base_api


@pytest.fixture
def root_dir(request):
    """项目根目录"""
    return request.config.rootpath


@pytest.fixture
def data_dir(root_dir):
    """数据目录"""
    return root_dir / 'data'

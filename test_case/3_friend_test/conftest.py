import pytest
from lib.base_view import BaseFun

b_fun = BaseFun()


# 拼接搜索好友地址
@pytest.fixture(scope='class')
def search_url(url):
    """
    :param url: 测试ip
    :return: 搜索好友接口
    """
    search_url = url + '/friend/search'
    return search_url


# 删除好友
@pytest.fixture(scope='function')
def delete_friend(base_fun, user_a, user_b):
    """
    :param base_fun: 继承基类
    :param user_a: 用户a登录
    :param user_b: 用户b登录
    :return: 请求结果
    """
    # 发送请求并获取返回值
    r = base_fun.delete_friend(user_a[0], user_b[2])
    return r


# 添加一个好友，然后删除
@pytest.fixture(scope='class')
def add_friend_and_delete(base_fun, user_a, user_b):
    """
    :param base_fun: 继承基类
    :param user_a: 用户a登录
    :param user_b: 用户b登录
    """
    # 添加好友
    base_fun.modify_user_setting(user_a[0], 1, 0)
    base_fun.add_friend(user_b[0], user_a[2], "I'm b.", 0)
    yield
    # 删除好友
    base_fun.delete_friend(user_b[0], user_a[2])


# 添加一个好友
@pytest.fixture(scope='function')
def add_friend(base_fun, user_a, user_b):
    """
    :param base_fun: 继承基类
    :param user_a: 用户a登录
    :param user_b: 用户b登录
    """
    # 修改添加好友设置
    base_fun.modify_user_setting(user_a[0], 1, 0)
    # 添加好友
    base_fun.add_friend(user_b[0], user_a[2], "I'm b.", 1)

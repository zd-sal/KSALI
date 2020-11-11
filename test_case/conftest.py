import pytest
from lib.base_view import BaseFun
import random
import logging


# 实例化公共接口与方法
@pytest.fixture(autouse=True, scope='module')
def base_fun():
    """
    :return: 绝对路径
    """
    bs_fun = BaseFun()
    return bs_fun


# 用户A的数据信息
@pytest.fixture(scope='class')
def payload_a(base_fun):
    """
    :param base_fun: 绝对路径
    :return: 用户参数
    """
    # 在ini文件中读取数据
    data = base_fun.make_user()
    payload = {'area_code': data['area_code'], 'short_name': data['short_name'], 'phone': data['A'],
               'password': data['password'], 'type': 1, 'verify_code': data['A'][2:8]}
    return payload


# 用户B的数据信息
@pytest.fixture(scope='class')
def payload_b(base_fun):
    """
    :param base_fun: 绝对路径
    :return: 用户参数
    """
    # 在ini文件中读取数据
    data = base_fun.make_user()
    payload = {'area_code': data['area_code'], 'short_name': data['short_name'], 'phone': data['B'],
               'password': data['password'], 'type': 1, 'verify_code': data['B'][2:8]}
    return payload


# 登录用户A
@pytest.fixture(scope="class")
def user_a(base_fun, payload_a):
    """
    :param base_fun: 绝对路径
    :param payload_a: 用户a参数
    :return: 请求头，云信id，用户id
    """
    logging.info('fixture:用户a登录')
    result = base_fun.sign_in(payload_a['area_code'], payload_a["phone"], payload_a['password'])
    # 拿到headers等返回值
    yunxin_id = result[2]
    headers = base_fun.header(result[1])
    user_id = result[4]
    return headers, yunxin_id, user_id


# 登录用户B
@pytest.fixture(scope="class")
def user_b(base_fun, payload_b):
    """
    :param base_fun: 绝对路径
    :param payload_b: 用户b参数
    :return: 请求头，云信id，用户id
    """
    logging.info('fixture:用户b登录')
    result = base_fun.sign_in(payload_b['area_code'], payload_b["phone"], payload_b['password'])
    yunxin_id = result[2]
    # 拿到headers等返回值
    headers = base_fun.header(result[1])
    user_id = result[4]
    return headers, yunxin_id, user_id


# 接口地址
@pytest.fixture(autouse=True, scope='class')
def url(base_fun):
    """
    :param base_fun: 继承基类
    :return: 测试ip
    """
    half_url = base_fun.half_url
    return half_url


# 创建一张创业圈图片
@pytest.fixture
def pic(base_fun):
    """
    :param base_fun: 继承基类
    :return: 图片，图片路径，图片名
    """
    logging.info('fixture:生成一张创业圈图片')
    # 生成图片
    pic = base_fun.pic_and_vid()
    return pic


# 创建一个视频
@pytest.fixture
def video(base_fun):
    """
    :param base_fun: 继承基类
    :return: 视频，视频路径，视频名
    """
    logging.info('fixture:生成创业圈视频')
    vid = base_fun.pic_and_vid('video')
    return vid


@pytest.fixture
def pics(base_fun):
    """
    :param base_fun: 继承基类
    :return: 图片列表，图片名和图片路径的字典，图片总量
    """
    logging.info('fixture:生成创业圈图片')
    number = random.randint(2, 9)
    pictures = base_fun.pic_and_vid(number)
    return pictures


# 获取资讯目录id
@pytest.fixture
def news_category_id(url, base_fun, user_a):
    """
    :param url: 测试ip
    :param base_fun: 继承基类
    :param user_a: 用户a登录
    :return: 资讯目录id
    """
    logging.info('fixture:获取资讯列表id')
    real_url = url + "/news/categories"
    payload = {}
    # 发送请求并获取返回值
    r = base_fun.send_request(real_url, payload, user_a[0])
    result = base_fun.json_loads(r.text)
    # 将目录id存入变量
    category_id = result['data'][0]['id']
    return category_id

#
# @pytest.fixture(scope='session', autouse=True)
# def pytest_sessionfinish(base_fun, payload_a, payload_b):
#     pass
#     yield
#     try:
#         i = 0
#         while i < 5:
#             print(i)
#             user_a = base_fun.sign_in(payload_a['area_code'], payload_a["phone"], payload_a['password'])
#             list = base_fun.personal_circle_list(user_a[1], '1', user_a[4])
#             result = base_fun.json_loads(list.text)
#             base_fun.delete_activity(user_a[1], result['data'][0]['id'])
#             i += 1
#     except:
#         i = 0
#         try:
#             while i < 5:
#                 print(i)
#                 user_b = base_fun.sign_in(payload_b['area_code'], payload_b["phone"], payload_b['password'])
#                 list = base_fun.personal_circle_list(user_b[1], '1', user_b[4])
#                 result = base_fun.json_loads(list.text)
#                 base_fun.delete_activity(user_b[1], result['data'][0]['id'])
#                 i += 1
#         except:
#             pass

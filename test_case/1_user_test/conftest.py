import pytest, logging


# 生成未注册手机号
@pytest.fixture(scope='class')
def unregistered_num(base_fun):
    """
    :param base_fun: 继承基类
    :return: 手机号
    """
    logging.info('fixture:生成未注册手机号')
    num = 0
    while num == 0:
        # 生成手机号
        phone = base_fun.create_phone()
        # 数据库查验
        result = base_fun.verify_it_in_db(phone)
        if result == 0:
            return phone
        else:
            continue


# 拼接设置用户信息url
@pytest.fixture
def set_url(url):
    """
    :param url: 测试ip
    :return: 用户设置接口
    """
    real_url = url + '/user/setUserInfo'
    return real_url


# 生成头像图片
@pytest.fixture
def head_img(base_fun):
    """
    :param base_fun: 继承基类
    :return: 图片，图片路径，图片名
    """
    # 创建图片
    logging.info('fixture:生称头像图片')
    pic = base_fun.headimg_cover('head')
    return pic

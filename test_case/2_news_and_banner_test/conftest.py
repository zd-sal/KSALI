import pytest,logging



# 获取资讯id
@pytest.fixture
def news_id(url, base_fun, user_a, news_category_id):
    """
    :param url: 测试ip
    :param base_fun: 继承基类
    :param user_a: 用户a登录
    :param news_category_id: 资讯目录id
    :return: 资讯id
    """
    real_url = url + '/news/list'
    payload = {'page': 1, 'category_id': news_category_id}
    # 发送请求并获取返回值
    logging.info('fixture:获取资讯列表')
    r = base_fun.send_request(real_url, payload, user_a[0])
    result = base_fun.json_loads(r.text)
    # 将资讯id存入变量
    logging.info('fixture:从资讯列表中拿到资讯')
    the_id = result['data'][0]['id']
    return the_id

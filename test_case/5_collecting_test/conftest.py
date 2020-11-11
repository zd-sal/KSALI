import pytest
import logging


# 发布图片动态
@pytest.fixture
def activity_pic(base_fun, user_b, pic):
    """
    :param base_fun: 继承基类
    :param user_b: 用户b登录
    :param pic: 图片
    :return: 文件内容
    """
    # 上传文件至oss
    base_fun.upload_file_to_oss(pic)
    # 发送请求并获取结果
    base_fun.add_activity(user_b[0], 'picture', feed_file=pic[0], the_type=2)
    # 发送请求并获取返回值
    r = base_fun.personal_circle_list(user_b[0], '1', user_b[2])
    result = base_fun.json_loads(r.text)
    # 拿到feed_file地址
    logging.info('fixture:从个人动态列表结果中拿到feed_file')
    content = str(result['data'][0]['feed_file'])
    # 拿到动态id
    logging.info('fixture:从个人动态列表结果中拿到feed_id')
    feed_id = result['data'][0]['id']
    yield content
    # 删除该动态
    base_fun.delete_activity(user_b[0], feed_id)


# 发布视频动态
@pytest.fixture
def activity_vid(base_fun, user_b, video):
    """
    :param base_fun: 继承基类
    :param user_b: 用户b登录
    :param video: 视频
    :return: 该文件内容
    """
    base_fun.upload_file_to_oss(video)
    # 发送请求并获取结果
    base_fun.add_activity(user_b[0], 'video', feed_file=video[0], the_type=3)
    # 发送请求并获取返回值
    r = base_fun.personal_circle_list(user_b[0], '1', user_b[2])
    result = base_fun.json_loads(r.text)
    # 拿到feed_file地址
    logging.info('fixture:从个人动态列表结果中拿到feed_file')
    content = str(result['data'][0]['feed_file'])
    # 拿到动态id
    logging.info('fixture:从个人动态列表结果中拿到feed_id')
    feed_id = result['data'][0]['id']
    yield content
    # 删除该动态
    base_fun.delete_activity(user_b[0], feed_id)


# 收藏图片，并获取id
@pytest.fixture
def collection_id(base_fun, user_b, url, activity_pic):
    """
    :param base_fun: 继承基类
    :param user_b: 用户b登录
    :param url: 测试ip
    :param activity_pic: 图片动态
    :return: 收藏文件的id
    """
    add_url = url + '/collection/add'
    payload = {'collectible_user_id': user_b[1], 'type': '1', 'content': activity_pic}
    # 发送请求,收藏图片
    logging.info('fixture:收藏一张创业圈图片')
    base_fun.send_request(add_url, payload, user_b[0])
    list_url = url + '/collection/list'
    payload = {'page': '1'}
    # 发送请求并获取返回值
    logging.info('fixture:获取收藏列表')
    r = base_fun.send_request(list_url, payload, user_b[0])
    result = base_fun.json_loads(r.text)
    # 拿到收藏id
    logging.info('fixture:从收藏列表拿到collection_id')
    collection_id = result['data'][0]['id']
    return collection_id

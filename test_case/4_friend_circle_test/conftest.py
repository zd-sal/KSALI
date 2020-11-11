import pytest, logging


# 发布一动态，并拿到id
@pytest.fixture(scope='class')
def feed_id(base_fun, user_b):
    """
    :param base_fun: 继承基类
    :param user_b: 用户b登录
    :return: 动态id
    """
    # 发送请求并获取返回值
    base_fun.add_activity(user_b[0], 'this is an activity for test', the_type=1)
    r = base_fun.personal_circle_list(user_b[0], '1', user_b[2])
    result = base_fun.json_loads(r.text)
    # 将动态id存入变量并返回
    logging.info('fixture:从个人动态列表拿到feed_id')
    feed_id = result['data'][0]['id']
    yield feed_id
    base_fun.delete_activity(user_b[0], feed_id)


# 发布一条动态评论，并拿到评论id
@pytest.fixture
def comment_id(base_fun, user_b, feed_id, comment_url):
    """
    :param base_fun: 继承基类
    :param user_b: 用户b登录
    :param feed_id: 动态id
    :param comment_url: 评论接口地址
    :return: 评论id
    """
    payload = {'feed_id': feed_id, 'reply_user': user_b[2], 'content': 'this is a comment for delete test'}
    # 发送请求
    base_fun.send_request(comment_url, payload, user_b[0])
    # 在个人创业圈列表拿到评论id
    r = base_fun.personal_circle_list(user_b[0], '1', user_b[2])
    result = base_fun.json_loads(r.text)
    # 将id传入变量
    logging.info('fixture:从个人创业圈列表拿到评论id')
    comment_id = result['data'][0]['comment'][0]['id']
    return comment_id


# 拼接点赞接口地址
@pytest.fixture
def like_url(url):
    """
    :param url: 测试ip
    :return: 点赞接口
    """
    like_url = url + '/feeds/like'
    return like_url


# 拼接评论接口地址
@pytest.fixture
def comment_url(url):
    """
    :param url: 测试ip
    :return: 评论接口
    """
    comment_url = url + '/feeds/comment-add'
    return comment_url


# 修改创业圈封面
@pytest.fixture
def change_feeds_cover(url, base_fun, user_a, cover):
    """
    :param url: 测试地址
    :param base_fun: 继承基类
    :param user_a: 用户a登录
    :param cover: 封面图
    :return: 状态码
    """
    real_url = url + '/feeds/changeCover'
    # 上传文件至oss
    base_fun.upload_file_to_oss(cover)
    payload = {'cover_image': cover[0]}
    # 发送请求并获取返回值
    logging.info('fixture:修改创业圈封面图')
    r = base_fun.send_request(real_url, user_a[0], payload)
    return r.status_code


# 资讯内容
@pytest.fixture
def news(url, base_fun, user_a, news_category_id):
    """
    :param url: 测试ip
    :param base_fun: 继承基类
    :param user_a: 用户a登录
    :param news_category_id: 资讯目录id
    :return: 资讯内容
    """
    # 拼接资讯列表接口
    real_url = url + '/news/list'
    # 请求数据
    payload = {'page': 1, 'category_id': news_category_id}  # 页数及资讯目录id
    # 发送请求并获取返回值
    r = base_fun.send_request(real_url, payload, user_a[0])
    result = base_fun.json_loads(r.text)
    try:
        # 拿到资讯内容
        logging.info('fixture:从资讯列表拿到资讯内容')
        share_image = result['data'][0]['photo']
        share_title = result['data'][0]['title']
        share_url = result['data'][0]['url']
        # 拼接字典
        contents = {"share_image": share_image, "share_title": share_title, "share_url": share_url}
        # json格式
        contents = base_fun.json_dumps(contents)
        return contents
    except KeyError:
        return '无资讯，请上传'


# 创建一张封面图片
@pytest.fixture
def cover(base_fun):
    """
    :param base_fun: 继承基类
    :return: 图片，图片路径，图片名
    """
    logging.info('fixture:获得一张头像图片')
    cover = base_fun.headimg_cover('cover')
    return cover


@pytest.fixture
def position(base_fun):
    location = base_fun.position()
    return location

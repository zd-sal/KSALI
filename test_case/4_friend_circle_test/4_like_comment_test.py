import pytest, allure, logging

'''
创业圈点赞与评论测试
'''


class TestCase:
    # 创业圈动态点赞
    @allure.feature('动态点赞与评论')
    @allure.story('点赞动态')
    @pytest.mark.run(order=1)
    def test_like(self, base_fun, user_b, feed_id, like_url):
        """
        :param base_fun: 继承基类
        :param user_b: 用户b登录
        :param feed_id: 创业圈动态id
        :param like_url: 点赞接口地址
        """
        payload = {'feed_id': feed_id}  # 动态id
        # 发送请求并获取结果
        logging.info('用例:点赞动态')
        r = base_fun.send_request(like_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 创业圈动态评论
    @allure.feature('动态点赞与评论')
    @allure.story('评论动态')
    @pytest.mark.run(order=2)
    def test_comment(self, base_fun, user_b, feed_id, comment_url):
        """
        :param base_fun: 继承基类
        :param user_b: 用户b登录
        :param feed_id: 创业圈动态id
        :param comment_url: 评论接口地址
        """
        payload = {'feed_id': feed_id, 'reply_user': user_b[2],
                   'content': 'this is a comment for test'}  # 动态id,回复用户id，回复内容
        # 发送请求并获取返回值
        logging.info('用例:评论动态')
        r = base_fun.send_request(comment_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 创业圈动态取消点赞
    @allure.feature('动态点赞与评论')
    @allure.story('取消点赞')
    @pytest.mark.run(order=3)
    def test_cancel_like(self, base_fun, url, user_b, feed_id, like_url):
        """
        :param base_fun: 继承基类
        :param url: 测试url
        :param user_b: 用户B登录
        :param feed_id: 创业圈动态id
        :param like_url: 点赞接口地址
        """
        payload = {'feed_id': feed_id}  # 动态id
        # 发送请求并获取动态id
        base_fun.send_request(like_url, payload, user_b[0])
        cancel_url = url + '/feeds/cancelLike'
        payload = {'feed_id': feed_id}
        # 发送请求并获取返回值
        logging.info('用例:取消点赞')
        r = base_fun.send_request(cancel_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 创业圈动态删除评论
    @allure.feature('动态点赞与评论')
    @allure.story('删除评论')
    @pytest.mark.run(order=4)
    def test_delete_comment(self, url, feed_id, base_fun, user_b, comment_id, comment_url):
        """
        :param url: 测试ip
        :param feed_id: 创业圈动态id
        :param base_fun: 继承基类
        :param user_b: 用户b登录
        :param comment_id: 评论id
        :param comment_url: 评论接口地址
        """
        delete_url = url + '/feeds/comment-delete'
        payload = {'comment_id': comment_id}  # 评论id
        logging.info('用例:删除评论')
        r = base_fun.send_request(delete_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)


if __name__ == '__main__':
    pytest.main('-s 4_like_comment_test.py')

import pytest, allure, logging

'''
获取好友信息测试
'''


class TestCase:
    # 获取好友信息
    @allure.feature('获取好友信息')
    @pytest.mark.run(order=1)
    def test_get_friend_info(self, url, user_a, user_b, base_fun, payload_b, add_friend):
        """
        :param url: 测试ip
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param base_fun: 继承基类
        :param payload_b: 用户A参数
        :param add_friend: 用例执行前，先添加好友
        """
        real_url = url + '/friend/getFriend'
        payload = {'friend_id': user_b[2]}  # 好友id
        # 发送请求并获取结果
        logging.info('用例:发送请求，获取好友信息')
        r = base_fun.send_request(real_url, payload, user_a[0])
        result2 = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert payload_b['phone'] == result2['data']['phone']
        assert user_b[2] == result2['data']['friend_id']

    # 获取好友设置
    @allure.feature('获取好友设置')
    @pytest.mark.run(order=2)
    def test_get_friend_settings(self, url, user_a, user_b, base_fun, add_friend):
        """
        :param url: 测试ip
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param base_fun: 继承基类
        :param add_friend: 用例执行前，先添加好友
        """
        real_url = url + '/friend/getFriendConfig'
        payload = {'friend_id': user_a[2]}
        # 发送请求并获取结果
        logging.info('用例:发送请求，获取好友设置')
        r = base_fun.send_request(real_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert user_a[2] == result['data']['friend_id']

    # 获取好友列表
    @allure.feature('获取好友列表')
    @pytest.mark.run(order=3)
    def test_get_friend_list(self, url, user_a, user_b, base_fun, add_friend):
        """
        :param url: 测试ip
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param base_fun: 继承基类
        :param add_friend: 用例执行前，先添加好友
        """
        real_url = url + '/friend/getFriendList'
        payload = {}
        # 发送请求并获取结果
        logging.info('用例:发送请求，获取好友列表')
        r = base_fun.send_request(real_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert str(user_a[2]) in str(result)


if __name__ == "__main__":
    pytest.main('-s test_get_friend_info.py')

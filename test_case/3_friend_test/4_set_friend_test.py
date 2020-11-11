import pytest, allure,logging

'''
好友备注与好友权限测试
'''


class TestCase:
    # 设置好友备注
    @allure.feature('设置好友备注')
    @pytest.mark.run(order=1)
    def test_set_friend_remark(self, url, user_a, user_b, base_fun, add_friend):
        """
        :param url: 测试ip
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param base_fun: 继承基类
        :param add_friend: 用例执行前，先添加好友
        """
        real_url = url + '/friend/setFriendRemark'
        payload = {'friend_id': user_b[2], 'remark_name': 'friend_b'}  # 好友id，和昵称内容
        # 发送请求并获取结果
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 设置好友权限（不让他看我）
    @allure.feature('设置好友权限')
    @allure.story('不让他看我')
    @pytest.mark.run(order=2)
    def test_set_friend_power_1(self, url, user_a, user_b, base_fun, add_friend):
        """
        :param url: 测试ip
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param base_fun: 继承基类
        :param add_friend: 用例执行前，先添加好友
        """
        real_url = url + '/friend/setFriendPower'
        payload = {'friend_id': user_b[2], 'type': 1, 'power': 1}
        # 发送请求并获取结果
        logging.info('用例:修改好友权限,(不让他看我)')
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 设置好友权限（我不看他）
    @allure.feature('设置好友权限')
    @allure.story('不让他看我')
    @pytest.mark.run(order=3)
    def test_set_friend_power_2(self, url, user_a, user_b, base_fun, add_friend):
        """
        :param url: 测试ip
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param base_fun: 继承基类
        :param add_friend: 用例执行前，先添加好友
        """
        real_url = url + '/friend/setFriendPower'
        payload = {'friend_id': user_b[2], 'type': 2, 'power': 1}
        # 发送请求并获取结果
        logging.info('用例:发送请求，修改好友权限,(我不看他)')
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)


if __name__ == "__main__":
    pytest.main('-s test_set_friend.py')

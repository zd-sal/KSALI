import pytest, allure,logging


class TestCase:
    # 添加好友设置
    @allure.feature('用户设置')
    @allure.story('修改好友添加设置')
    @pytest.mark.run(order=1)
    def test_set_friend(self, user_a, base_fun):
        """
        :param user_a: 用户a登录
        :param base_fun: 继承基类
        """
        # 发送请求并获取返回值
        logging.info('用例:修改添加好友设置')
        r = base_fun.modify_user_setting(user_a[0], 1, 1)  # 用户token和字段的值
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 添加群设置修改
    @allure.feature('用户设置')
    @allure.story('修改群添加设置')
    @pytest.mark.run(order=2)
    def test_set_group(self, user_a, base_fun):
        """
        :param user_a: 用户a登录
        :param base_fun: 继承基类
        """
        # 发送请求并获取返回值
        logging.info('用例:修改添加群设置')
        r = base_fun.modify_user_setting(user_a[0], 2, 1)  # 用户token和字段的值
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 获取设置信息
    @allure.feature('用户设置')
    @allure.story('获取设置信息')
    @pytest.mark.run(order=3)
    def test_get_config(self, user_a, base_fun, url):
        """
        :param user_a: 用户a登录
        :param base_fun: 继承基类
        :param url: 测试ip
        """
        real_url = url + '/user/getUserConfig'
        payload = {}
        # 发送请求并获取返回值
        logging.info('用例:获取设置信息')
        r = base_fun.send_request(real_url, payload, user_a[0])  # 接口地址，用户token
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'add_friend_authentication' in str(result)


if __name__ == '__main__':
    pytest.main('-s test_set_user_config.py')

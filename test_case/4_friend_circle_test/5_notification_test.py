import pytest, allure, logging

'''
创业圈通知测试
'''


class TestCase:
    # 获取通知
    @allure.feature('创业圈通知')
    @allure.story('获取通知')
    @pytest.mark.run(order=1)
    def test_notice(self, url, base_fun, user_a):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        """
        # 拼接通知接口地址
        real_url = url + "/notification/info"
        payload = {}
        logging.info('用例:获取创业圈通知')
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert r.status_code
        assert 'success' in str(result)

    # 获取通知列表
    @allure.feature('创业圈通知')
    @allure.story('获取通知列表')
    @pytest.mark.run(order=2)
    def test_notification_list(self, url, base_fun, user_b):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_b: 用户b登录
        """
        # 拼接通知列表接口地址
        real_url = url + "/notification/list"
        payload = {}
        # 发送请求并获取返回值
        logging.info('用例:获取创业圈通知列表')
        r = base_fun.send_request(real_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert r.status_code
        assert 'success' in str(result)


if __name__ == "__main__":
    pytest.main('-s test_notification.py')

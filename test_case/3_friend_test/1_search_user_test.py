import pytest, allure, logging

'''
搜索好友测试
'''


class TestCase:
    # 搜索好友
    @allure.feature('搜索好友')
    @allure.story('手机号搜索好友')
    @allure.severity("critical")
    @pytest.mark.run(order=1)
    def test_search_user(self, search_url, base_fun, user_a, payload_b):
        """
        :param search_url: 搜索好友接口
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param payload_b: 用户A参数
        """
        payloads = {'keyword': payload_b['phone'], 'type': '0'}  # 用户手机号和type值
        # 发送请求并获取结果
        logging.info('用例:搜索好友')
        r = base_fun.send_request(search_url, payloads, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert payload_b['phone'] == result['data']['phone']

    # 扫描好友二维码
    @allure.feature('搜索好友')
    @allure.story('扫描二维码搜索好友')
    @allure.severity("critical")
    @pytest.mark.run(order=2)
    @pytest.mark.skip
    def test_scan_user(self, search_url, base_fun, user_a, user_b, payload_b):
        """
        :param search_url: 搜索好友接口
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param payload_b: 用户A参数
        """
        payloads = {'keyword': "902e51b7a9f5489502b1aab197558c61", 'type': '1'}  # 用户扫码的值和type值
        # 发送请求并获取结果
        r = base_fun.send_request(search_url, payloads, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert payload_b['phone'] == result['data']['phone']


if __name__ == '__main__':
    pytest.main(['-s', '1_search_user_test.py'])

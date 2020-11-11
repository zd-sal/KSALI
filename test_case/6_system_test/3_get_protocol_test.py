import pytest, allure, logging


class TestCase:
    @allure.feature('获取协议')
    @allure.story('用户使用协议')
    @pytest.mark.run(order=1)
    # 获取用户使用协议
    def test_get_using_protocol(self, url, base_fun, payload_a):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param payload_a: 用户a参数
        """
        url = url + '/system/getProtocol'
        payload = {'type': 1, 'short_name': payload_a['short_name']}  # type值 和 地区简称
        logging.info('用例:获取用户使用协议')
        r = base_fun.send_request(url, payload)
        result = base_fun.json_loads(r.text)
        assert 200 == r.status_code
        assert 'content' in str(result)

    @allure.feature('获取协议')
    @allure.story('隐私协议')
    @pytest.mark.run(order=2)
    # 获取隐私协议
    def test_get_privacy_protocol(self, url, base_fun, payload_a):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param payload_a: 用户a参数
        """
        # 拼接url
        url = url + '/system/getProtocol'
        # 发送请求并获取结果
        payload = {'type': 2, 'short_name': payload_a['short_name']}  # type值 和 地区简称
        logging.info('用例:获取隐私协议')
        r = base_fun.send_request(url, payload)
        result = base_fun.json_loads(r.text)
        # 断言结果
        assert 200 == r.status_code
        assert 'content' in str(result)


if __name__ == '__main__':
    pytest.main()

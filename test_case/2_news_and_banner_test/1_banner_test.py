import pytest, allure,logging
'''
Banner图测试
'''


class TestCase:
    # 获取Banner图
    @allure.feature('获取Banner图')
    @allure.severity("critical")
    @pytest.mark.run(order=1)
    def test_banner(self, url, user_a, base_fun):
        """
        :param url: 测试ip
        :param user_a: 用户a登录
        :param base_fun: 继承基类
        """
        banner_url = url + '/banner/list'
        payload = {}
        # 发送请求并获取返回值
        logging.info('用例:获取banner列表')
        r = base_fun.send_request(banner_url, payload, user_a[0])  # 接口url，用户token
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' and 'image' in str(result)


if __name__ == '__main__':
    pytest.main(['1_banner_test.py'])

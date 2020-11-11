import pytest, allure, logging


class TestCase:
    @allure.feature('获取语言包')
    # 获取语言包
    def test_language_package(self, url, base_fun):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        """
        # 拼接url
        url = url + '/system/language'
        # 发送请求并获取结果
        logging.info('用例:获取语言包')
        r = base_fun.send_request(url)
        result = base_fun.json_loads(r.text)
        # 断言结果
        assert 200 == r.status_code
        assert 'short_name' in str(result)


if __name__ == '__main__':
    pytest.main()

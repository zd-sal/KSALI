import pytest, allure, logging


class TestCase:
    @allure.feature('获取安卓升级包')
    # 获取安卓升级包
    def test_get_android_update(self, url, base_fun):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        """
        # 拼接url
        url = url + '/system/getSdk'
        # 发送请求
        logging.info('用例:获取安卓升级包')
        r = base_fun.send_request(url)
        # 发送请求并获取结果
        result = base_fun.json_loads(r.text)
        # 断言结果
        assert 200 == r.status_code
        assert 'version_name' or 'success' in str(result)


if __name__ == '__main__':
    pytest.main(['-s'])

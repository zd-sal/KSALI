import pytest, allure, logging


class TestCase:
    @allure.feature('获取oss信息')
    @pytest.mark.skip('暂未使用')
    # 获取oss信息
    def test_get_oss_info(self, url, user_a, base_fun):
        """
        :param url: 测试ip
        :param user_a: 用户a登录
        :param base_fun: 继承基类
        """
        # 拼接url
        url = url + '/system/getOssInfo'
        # 发送请求并获取结果
        logging.info('用例:获取oss信息')
        r = base_fun.send_request(url, user_a[0])  # url及token
        result = base_fun.json_loads(r.text)
        # 断言结果
        assert 200 == r.status_code
        assert 'SecurityToken' in str(result)


if __name__ == '__main__':
    pytest.main()

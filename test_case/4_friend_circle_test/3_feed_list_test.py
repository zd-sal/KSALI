import pytest, allure,logging

'''
创业圈列表测试
'''


class TestCase:
    # 获取创业圈动态列表
    @allure.feature('获取创业圈动态列表')
    @allure.story('创业圈动态列表')
    @allure.severity("critical")
    @pytest.mark.run(order=1)
    def test_feed_list(self, url, base_fun, user_a):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_a: 用户a登录
        """
        real_url = url + '/feeds/list'
        # 请求数据
        payload = {'page': '1'}  # 页数
        logging.info('用例:获取创业圈动态列表')
        # 发送请求并获取结果
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 获取个人创业圈动态列表
    @allure.feature('获取创业圈动态列表')
    @allure.story('个人创业圈动态列表')
    @pytest.mark.run(order=2)
    def test_personal_feed_list(self, base_fun, user_a):
        """
        :param base_fun: 继承基类
        :param user_a: 用户a登录
        """
        # 发送请求并获取结果
        r = base_fun.personal_circle_list(user_a[0], '1', user_a[2])  # 传入token 和页数及用户id
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)
        assert 'feed_content' in str(result)


if __name__ == '__main__':
    pytest.main('-s test_feed_list.py')

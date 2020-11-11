import pytest, allure, logging

'''
资讯测试
'''


class TestCase:
    # 获取资讯目录
    @allure.feature('资讯')
    @allure.story('获取资讯目录')
    @allure.severity("critical")
    @pytest.mark.run(order=1)
    def test_news_category(self, url, base_fun, user_a):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_a: 用户a登录
        """
        real_url = url + "/news/categories"
        payload = {}
        # 发送请求并获取返回值
        logging.info('用例:获取资讯目录')
        r = base_fun.send_request(real_url, payload, user_a[0])  # 接口url 和用户token
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 获取资讯列表
    @allure.feature('资讯')
    @allure.story('获取资讯列表')
    @allure.severity("critical")
    @pytest.mark.run(order=2)
    def test_news_list(self, url, base_fun, user_a, news_category_id):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_a: 用户a登录
        :param news_category_id: 资讯列表id
        """
        real_url = url + '/news/list'
        payload = {'page': 1, 'category_id': news_category_id}  # 页数，和目录id
        # 发送请求并获取返回值
        logging.info('用例：获取资讯列表')
        r = base_fun.send_request(real_url, payload, user_a[0])  # 接口url ,请求数据和用户token
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' and 'create_time' in str(result)

    # 获取资讯详情
    @allure.feature('资讯')
    @allure.story('获取资讯详情')
    @allure.severity("critical")
    @pytest.mark.run(order=3)
    def test_news_detail(self, url, base_fun, user_a, news_id):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_a: 用户a登录
        :param news_id: 资讯id
        """
        real_url = url + '/news/view'
        payload = {'id': news_id}  # 资讯id
        # 发送请求并获取返回值
        logging.info('用例：获取资讯详情')
        r = base_fun.send_request(real_url, payload, user_a[0])  # 接口url ,请求数据和用户token
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert news_id == result['data']['id']
        assert 'success' and 'create_time' in str(result)


if __name__ == '__main__':
    pytest.main(['-s', '2_news_test.py'])

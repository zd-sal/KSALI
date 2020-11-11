import pytest, allure, logging

'''
收藏测试
'''


class TestCase:
    # 添加创业圈图片至收藏
    @allure.feature('添加收藏')
    @allure.story('添加图片')
    @pytest.mark.run(order=1)
    def test_add_collection_pic(self, url, base_fun, user_b, activity_pic):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_b: 用户b登录
        :param activity_pic: 动态图片
        """
        real_url = url + "/collection/add"
        payload = {'collectible_user_id': user_b[2], 'type': '1', 'content': activity_pic}  # 用户id，type值，及收藏的文件
        # 发送请求并获取结果
        logging.info('发送请求，添加收藏一张创业圈图片')
        r = base_fun.send_request(real_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言结果
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 添加创业圈视频至收藏
    @allure.feature('添加收藏')
    @allure.story('添加视频')
    @pytest.mark.run(order=2)
    def test_add_collection_vid(self, url, base_fun, user_b, activity_vid):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_b: 用户b登录
        :param activity_vid: 动态视频
        """
        real_url = url + '/collection/add'
        payload = {'collectible_user_id': user_b[2], 'type': '2', 'content': activity_vid}  # 用户id，type值，及收藏的文件
        # 发送请求并获取结果
        logging.info('发送请求，添加收藏一张创业圈视频')
        r = base_fun.send_request(real_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言结果
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 获取收藏列表
    @allure.feature('获取收藏列表')
    @pytest.mark.run(order=3)
    def test_collection_list(self, url, base_fun, user_b):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_b: 用户b登录
        """
        real_url = url + '/collection/list'
        payload = {'page': '1'}  # 列表页数
        # 发送请求并获取结果
        logging.info('发送请求，获取收藏列表')
        r = base_fun.send_request(real_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言结果
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 删除收藏条目
    @allure.feature('删除收藏条目')
    @pytest.mark.run(order=4)
    def test_delete_collection(self, url, base_fun, user_b, collection_id):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_b: 用户b登录
        :param collection_id: 已收藏文件id
        """
        real_url = url + '/collection/delete'
        payload = {'collection_id': collection_id}  # 收藏条目的id
        # 发送请求并获取结果
        logging.info('发送请求，删除收藏图片')
        r = base_fun.send_request(real_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言结果
        assert 200 == r.status_code
        assert 'success' in str(result)


if __name__ == '__main__':
    pytest.main('-s test_collection.py')

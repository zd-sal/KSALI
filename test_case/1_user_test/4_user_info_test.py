import pytest, allure,logging


class TestCase:
    # 修改用户昵称
    @allure.feature('修改用户信息')
    @allure.story('修改昵称')
    @pytest.mark.run(order=1)
    def test_change_user_nickname(self, set_url, base_fun, user_a):
        """
        :param set_url: 修改用户信息的接口
        :param base_fun: 继承的基类
        :param user_a: 用户A登录
        """
        payload = {'keyword': 'A', 'type': '1'}  # 想要修改的昵称及type值
        # 发送请求并获取返回值
        logging.info('用例:修改昵称')
        r = base_fun.send_request(set_url, payload, user_a[0])
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(r.text)

    # 修改用户性别
    @allure.feature('修改用户信息')
    @allure.story('修改性别')
    @pytest.mark.run(order=2)
    def test_change_user_sex(self, set_url, base_fun, user_a):
        """
        :param set_url: 修改用户信息的接口
        :param base_fun: 继承的基类
        :param user_a: 用户A登录
        """
        payload = {'keyword': '1', 'type': '2'}  # 性别对应的数字及type值
        # 发送请求并获取返回值
        logging.info('用例:修改性别')
        r = base_fun.send_request(set_url, payload, user_a[0])
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(r.text)

    # 修改用户个性签名
    @allure.feature('修改用户信息')
    @allure.story('修改个性签名')
    @pytest.mark.run(order=3)
    def test_change_user_signature(self, set_url, base_fun, user_a):
        """
        :param set_url: 修改用户信息的接口
        :param base_fun: 继承的基类
        :param user_a: 用户A登录
        """
        payload = {'keyword': 'This is it.', 'type': '3'}  # 个性签名内容及type值
        # 发送请求并获取返回值
        logging.info('用例:修改个性签名')
        r = base_fun.send_request(set_url, payload, user_a[0])
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(r.text)

    # 修改用户头像
    @allure.feature('修改用户信息')
    @allure.story('修改头像')
    @pytest.mark.run(order=4)
    def test_set_head_image(self, url, base_fun, user_a, head_img):
        """
        :param url: 测试ip
        :param base_fun: 继承的基类
        :param user_a: 用户A登录
        :param head_img: 一张图片
        """
        real_url = url + "/user/setHeadImg"
        # 上传至oss
        base_fun.upload_file_to_oss(head_img)
        payload = {'head_img': head_img[0]}  # 图片
        # 发送请求并获取返回值
        logging.info('用例:修改用户头像')
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 获取用户信息
    @allure.feature('获取用户信息')
    @allure.story('获取信息')
    @pytest.mark.run(order=5)
    def test_get_user_info(self, url, base_fun, user_a):
        """
        :param url: 测试ip
        :param base_fun:继承的基类
        :param user_a:用户A登录
        """
        real_url = url + '/user/getUserInfo'
        payload = {}
        # 发送请求并获取返回值
        logging.info('用例:获取用户信息')
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 1 == result['data']['sex']
        assert 'A' == result['data']['nickname']
        assert 'This is it.' == result['data']['personal_signature']

    # 经yunxin_id获取用户信息
    @allure.feature('获取用户信息')
    @allure.story('使用yunxin_id获取信息')
    @pytest.mark.run(order=6)
    def test_get_info_by_yunxin_id(self, url, base_fun, user_a):
        """
        :param url: 测试ip
        :param base_fun:继承的基类
        :param user_a:用户A登录
        """
        real_url = url + '/user/userInfo'
        payload = {'yunxin_id': user_a[1]}
        # 发送请求并获取返回值
        logging.info('用例:yunxin_id获取用户信息')
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert '53445525' == result['data']['phone']
        assert 'HK' == result['data']['short_name']

    # 获取粉丝列表
    @allure.feature('获取粉丝列表')
    @pytest.mark.run(order=7)
    def test_my_fans(self, url, base_fun, user_a):
        """
        :param url: 测试ip
        :param base_fun:继承的基类
        :param user_a:用户A登录
        """
        real_url = url + '/user/getFansList'
        payload = {'page': '1', 'keyword': ''}
        # 发送请求并获取返回值
        logging.info('用例:获取粉丝列表')
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)


if __name__ == "__main__":
    pytest.main(['-s'])

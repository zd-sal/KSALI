import pytest, allure


class TestCase:
    @allure.feature('发送登录验证码')
    @allure.story('登录验证码')
    @pytest.mark.run(order=1)
    def test_send_code_login(self, base_fun, payload_a):
        """
        :param base_fun: 继承的方法类
        :param payload_a: 用户a的参数
        """
        # 发送请求并获取返回值
        r = base_fun.get_verify_code(payload_a['area_code'], payload_a['phone'], 1)  # 传入区号和手机号及TYPE值
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert '10114' in str(result)

    @allure.feature('发送登录验证码')
    @allure.story('未注册账号登录验证码')
    @pytest.mark.run(order=2)
    def test_send_code_login(self, base_fun, payload_a, unregistered_num):
        """
        :param base_fun: 继承的方法类
        :param payload_a: 用户a的参数
        :param unregistered_num: 一个未注册的账号
        """
        # 发送请求并获取返回值
        r = base_fun.get_verify_code(payload_a['area_code'], unregistered_num, 1)  # 传入区号和随机手机号及TYPE值
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert '10114' in str(result)

    @allure.feature('发送注册验证码')
    @allure.story('未注册账号发送验证码')
    @pytest.mark.run(order=3)
    def test_send_code_sign_up(self, base_fun, payload_a, unregistered_num):
        """
        :param base_fun: 继承的方法类
        :param payload_a: 用户a的参数
        :param unregistered_num: 一个未注册的账号
        """
        # 发送请求并获取返回值
        r = base_fun.get_verify_code(payload_a['area_code'], unregistered_num, 2)  # 传入区号和随机手机号及TYPE值
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    @allure.feature('发送注册验证码')
    @allure.story('已注册账号发送验证码')
    @pytest.mark.run(order=4)
    def test_used_phone_sign_up(self, base_fun, payload_a):
        """
        :param base_fun: 继承的方法类
        :param payload_a: 用户a的参数
        """
        # 发送请求并获取返回值
        base_fun.sign_in(payload_a['area_code'], payload_a['phone'], payload_a['password'])  # 传入区号和手机号及密码
        r = base_fun.get_verify_code(payload_a['area_code'], payload_a['phone'], 2)
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert '10115' in str(result)

    @allure.feature('修改密码验证码')
    @pytest.mark.run(order=5)
    def test_send_code_change_password(self, base_fun, payload_a):
        """
        :param base_fun: 继承的方法类
        :param payload_a: 用户a的参数
        """
        # 发送请求并获取返回值
        r = base_fun.get_verify_code(payload_a['area_code'], payload_a['phone'], 3)  # 传入区号和随机手机号及TYPE值
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    @allure.feature('验证验证码')
    @pytest.mark.run(order=6)
    def test_verify_verifycode(self, base_fun, payload_a):
        """
        :param base_fun: 继承的方法类
        :param payload_a: 用户a的参数
        :return:
        """
        # 发送验证码
        base_fun.get_verify_code(payload_a['area_code'], payload_a['phone'], 1)
        # 发送请求并获取返回值
        r = base_fun.verifying_the_code(payload_a['area_code'], payload_a['phone'], 1, payload_a['verify_code'])  # 区号和手机号和TYPE值及密码
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)


if __name__ == '__main__':
    pytest.main(['-s'])
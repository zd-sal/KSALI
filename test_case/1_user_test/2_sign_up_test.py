import pytest, allure


class TestCase:
    # 注册测试
    @allure.feature('注册接口测试')
    @pytest.mark.run(order=1)
    @pytest.mark.skip
    def test_sign_up(self, base_fun, payload_a, unregistered_num):
        """
        :param base_fun: 继承的基类
        :param payload_a: 用户a的参数
        :param unregistered_num: 一个未注册的账号
        """
        # 获取验证码
        base_fun.get_verify_code(payload_a['area_code'], unregistered_num, 2)
        # 验证验证码
        base_fun.verifying_the_code(payload_a['area_code'], unregistered_num, 2, payload_a['verify_code'])
        # 发送请求并获取返回值
        r = base_fun.sign_up(payload_a['area_code'], payload_a['short_name'], unregistered_num,
                             payload_a['password'], payload_a['verify_code'])  # 传入区号及手机号等信息
        # 断言返回值
        assert 200 == r[0]
        assert unregistered_num == r[1]

    # 邀请接口测试
    @allure.feature('邀请接口测试')
    @pytest.mark.run(order=2)
    @pytest.mark.skip
    def test_invited_by(self, url, payload_a, unregistered_num, base_fun):
        """
        :param url: 传入测试ip
        :param payload_a: 用户a的参数
        :param unregistered_num: 一个未注册的账号
        :param base_fun: 继承的基类
        """
        real_url = url + '/user/invitedByPhone'
        result = base_fun.sign_in(payload_a['area_code'], unregistered_num, payload_a['password'])# 传入区号及手机号等信息
        # 拿到token
        token = result[1]
        real_payload = {'invite_telephone': payload_a['phone']}
        # 拼接header
        header = base_fun.header(token)
        # 发送请求并获取返回值
        r = base_fun.send_request(real_url, real_payload, header)
        # 断言返回值
        assert r.status_code == 200
        assert "yunxin_id" in str(r.text)


if __name__ == '__main__':
    pytest.main()

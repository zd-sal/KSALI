import pytest, allure,logging


# 登录
@allure.feature('登录测试')
@allure.story('普通登录')
@pytest.mark.run(order=1)
def test_login(payload_a, base_fun):
    """
    :param payload_a: 用户A的参数
    :param base_fun: 继承的基类
    """
    # 发送请求并获取返回值
    result = base_fun.sign_in(payload_a['area_code'], payload_a['phone'], payload_a['password'])  # 传入区号及手机号等信息
    # 断言返回值
    assert payload_a['phone'] == result[3]
    assert 200 == result[0]


@allure.feature('登录测试')
@allure.story('错误密码登录')
@pytest.mark.run(order=2)
def test_login_wrong_pwd(payload_a, base_fun, url):
    """
    :param payload_a: 用户A的参数
    :param base_fun: 继承的基类
    :param url: 测试ip
    """
    # 登录地址
    real_url = url + "/user/login"
    # 登录数据
    payload = {'area_code': payload_a['area_code'], 'phone': payload_a['phone'], 'password': '000000'}  # 传入区号及手机号等信息
    # 发送请求并获取返回值
    r = base_fun.send_request(real_url, payload)
    result = base_fun.json_loads(r.text)
    # 断言返回值
    assert 200 == r.status_code
    assert '10104' in str(result)


# 使用验证码登录
@allure.feature('登录测试')
@allure.story('验证码登录')
@pytest.mark.run(order=3)
def test_login_by_code(payload_a, base_fun):
    """
    :param payload_a: 用户A的参数
    :param base_fun: 继承的基类
    """
    # 发送验证码
    base_fun.get_verify_code(payload_a['area_code'], payload_a['phone'], payload_a['type'])
    # 验证验证码
    base_fun.verifying_the_code(payload_a['area_code'], payload_a['phone'], payload_a['type'],
                                payload_a['verify_code'])  # 传入区号及手机号等信息
    # 发送请求并获取返回值
    r = base_fun.sign_in_by_code(payload_a['area_code'], payload_a['phone'], payload_a['verify_code'])
    result = base_fun.json_loads(r.text)
    # 断言返回值
    assert 200 == r.status_code
    assert payload_a['phone'] == result['data']['phone']


# 使用验证码登录
@allure.feature('登录测试')
@allure.story('错误验证码登录')
@pytest.mark.run(order=4)
def test_login_by_wrong_code(payload_a, base_fun):
    """
    :param payload_a: 用户A的参数
    :param base_fun: 继承的基类
    """
    # 发送验证码
    base_fun.get_verify_code(payload_a['area_code'], payload_a['phone'], payload_a['type'])  # 传入区号及手机号等信息
    # 验证验证码
    base_fun.verifying_the_code(payload_a['area_code'], payload_a['phone'], payload_a['type'],
                                payload_a['verify_code'])  # 传入区号及手机号等信息
    # 发送请求并获取返回值
    r = base_fun.sign_in_by_code(payload_a['area_code'], payload_a['phone'], '000000')  # 传入区号及手机号等信息
    result = base_fun.json_loads(r.text)
    # 断言返回值
    assert 200 == r.status_code
    assert '10106' in str(result)


@allure.feature('修改密码测试')
@pytest.mark.run(order=5)
def test_change_password(payload_a, base_fun, url, user_a):
    """
    :param payload_a: 用户A的参数
    :param base_fun: 继承的基类
    :param url: 测试ip
    :param user_a: 用户A登录
    """
    # 发送验证码
    base_fun.get_verify_code(payload_a['area_code'], payload_a['phone'], 3)
    # 验证验证码
    base_fun.verifying_the_code(payload_a['area_code'], payload_a['phone'], 3, payload_a['verify_code'])
    # 拼接请求地址
    url = url + '/user/forgetPw'
    # 请求参数
    payload = {'phone': payload_a['phone'], 'area_code': payload_a['area_code'], 'password': payload_a['password'],
               'verify_code': payload_a['verify_code']}
    # 发送请求并获取返回值
    logging.info('用例:修改密码')
    r = base_fun.send_request(url, payload, user_a[0])
    result = base_fun.json_loads(r.text)
    # 断言返回值
    assert 200 == r.status_code
    assert 'success' in str(result)


# 退出登录测试
@allure.feature('退出登录测试')
@pytest.mark.run(order=6)
def test_log_out(user_a, base_fun):
    """
    :param user_a: 用户A登录
    :param base_fun: 继承的基类
    """
    # 发送请求并获取返回值
    r = base_fun.log_out(user_a[0])
    result = base_fun.json_loads(r.text)
    # 断言返回值
    assert 200 == r.status_code
    assert 'success' in str(result)


if __name__ == '__main__':
    pytest.main()

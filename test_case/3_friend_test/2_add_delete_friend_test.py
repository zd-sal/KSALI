import pytest, allure

'''
添加与删除好友测试
'''


class TestCase:
    # 搜索添加好友
    @allure.feature('添加好友')
    @allure.story('搜索添加好友')
    @allure.severity("critical")
    @pytest.mark.run(order=1)
    def test_add_friend_by_search(self, base_fun, user_a, user_b, delete_friend):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param delete_friend: 该用例执行前，先删除好友
        """
        # 发送请求并获取结果
        r = base_fun.add_friend(user_a[0], user_b[2], "I'm A.", 2)  # 用户token 和另一个用户的id，和发送内容及type值
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 扫描添加好友
    @allure.feature('添加好友')
    @allure.story('扫面添加好友')
    @allure.severity("critical")
    @pytest.mark.run(order=2)
    def test_add_friend_by_scan(self, base_fun, user_a, user_b, delete_friend):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param delete_friend: 该用例执行前，先删除好友
        """
        # 发送请求并获取结果
        r = base_fun.add_friend(user_a[0], user_b[2], "I'm A.", 4)  # 用户token 和另一个用户的id，和发送内容及type值
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 群添加好友
    @allure.feature('添加好友')
    @allure.story('群添加好友')
    @pytest.mark.run(order=3)
    def test_add_friend_by_group(self, base_fun, user_a, user_b, delete_friend):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param delete_friend: 该用例执行前，先删除好友
        """
        # 发送请求并获取结果
        r = base_fun.add_friend(user_a[0], user_b[2], "I'm A.", 3)  # 用户token 和另一个用户的id，和发送内容及type值
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 名片添加好友
    @allure.feature('添加好友')
    @allure.story('名片添加好友')
    @pytest.mark.run(order=3)
    def test_add_friend_by_id_card(self, base_fun, user_a, user_b, delete_friend):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param delete_friend: 该用例执行前，先删除好友
        """
        # 发送请求并获取结果
        r = base_fun.add_friend(user_a[0], user_b[2], "I'm A.", 1)  # 用户token 和另一个用户的id，和发送内容及type值
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 通过好友验证
    @allure.feature('通过好友申请')
    @pytest.mark.run(order=4)
    @allure.severity("critical")
    def test_adding_friend_apply(self, base_fun, user_a, user_b, delete_friend):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param delete_friend: 该用例执行前，先删除好友
        """
        # 发送请求并获取结果
        r = base_fun.add_friend_apply(user_b[0], user_a[1])  # 用户token 和另一个用户的yunxin_id
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 删除好友
    @allure.feature('删除好友')
    @pytest.mark.run(order=5)
    def test_delete_friend(self, base_fun, user_a, user_b, add_friend):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param user_b: 用户B登录
        :param add_friend: 该用例执行前，先添加好友
        """
        # 发送请求并获取结果
        r = base_fun.delete_friend(user_a[0], user_b[2])  # 用户token，和另一个用户的id
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)


if __name__ == "__main__":
    pytest.main('-s test_add_friend.py')

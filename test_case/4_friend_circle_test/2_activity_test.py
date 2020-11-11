import pytest, allure, logging

'''
创业圈动态测试
'''


class TestCase:
    # 发布创业圈文本动态
    @allure.feature('发布创业圈动态')
    @allure.story('文本动态')
    @allure.severity("critical")
    @pytest.mark.run(order=1)
    def test_add_activity_text(self, base_fun, user_a):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        """
        # 发送请求并获取结果
        r = base_fun.add_activity(user_a[0], 'testing content', the_type=1)  # 传入文本内容和type
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)
    # 发布创业圈文本动态
    @allure.feature('发布创业圈动态')
    @allure.story('带地址的文本动态')
    @allure.severity("critical")
    @pytest.mark.run(order=2)
    def test_add_activity_text_with_location(self, base_fun, user_a, position):
        """
        :param base_fun: 继承基类
        :param user_a: 用户a登录
        :param position: 地址信息
        """
        # 发送请求并获取结果
        r = base_fun.add_activity(user_a[0], 'testing content', the_type=1, address=position[2],
                                  latitude=position[0], longitude=position[1])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 发布创业圈图片动态
    @allure.feature('发布创业圈动态')
    @allure.story('图片动态')
    @allure.severity("critical")
    @pytest.mark.run(order=3)
    def test_add_activity_photo(self, base_fun, user_a, pic):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param pic: 图片
        """
        # 上传文件至oss
        base_fun.upload_file_to_oss(pic)
        # 发送请求并获取结果
        r = base_fun.add_activity(user_a[0], 'picture', feed_file=pic[0], the_type=2)  # 传入图片和type
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    @allure.feature('发布创业圈动态')
    @allure.story('多张图片动态')
    @allure.severity("critical")
    @pytest.mark.run(order=4)
    def test_add_multiple_photos(self, base_fun, user_a, pics):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param pic: 图片
        """
        # 遍历图片并上传
        base_fun.upload_file_to_oss(pics)
        r = base_fun.add_activity(user_a[0], 'picture', feed_file=pics[0], the_type=2)  # 传入图片和type
        result = base_fun.json_loads(r.text)
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 发布创业圈视频动态
    @allure.feature('发布创业圈动态')
    @allure.story('视频动态')
    @allure.severity("critical")
    @pytest.mark.run(order=5)
    def test_add_activity_video(self, base_fun, user_a, video):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param video: 视频
        """
        base_fun.upload_file_to_oss(video)
        # 发送请求并获取结果
        r = base_fun.add_activity(user_a[0], 'video', feed_file=video[0], the_type=3)  # 传入视频和type
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 发布创业圈资讯动态
    @allure.feature('发布创业圈动态')
    @allure.story('资讯动态')
    @allure.severity("critical")
    @pytest.mark.run(order=6)
    def test_add_activity_news(self, base_fun, user_a, news):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param news: 资讯
        """
        # 发送请求并获取结果
        r = base_fun.add_activity(user_a[0], 'this is a news', share_content=news, the_type=4)  # 传入资讯和type
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 删除创业圈动态
    @allure.feature('删除创业圈动态')
    @pytest.mark.run(order=7)
    def test_delete_activity(self, base_fun, user_b):
        """
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        """

        # 添加一条创业圈动态
        base_fun.add_activity(user_b[0], 'this is a delete test', the_type=1)
        # 发送请求并获取结果
        r = base_fun.personal_circle_list(user_b[0], '1', user_b[2])
        result = base_fun.json_loads(r.text)
        feed_id = result['data'][0]['id']
        # 将上一个请求的结果传至下一个请求，并发送
        r = base_fun.delete_activity(user_b[0], feed_id)  # 传入用户token 和 动态id
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 进入动态详情
    @allure.feature('进入动态详情')
    @pytest.mark.run(order=8)
    def test_activity_detail(self, url, base_fun, user_b, feed_id):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_b: 用户B登录
        :param feed_id: 动态ID
        """
        real_url = url + '/feeds/view'
        payload = {'feed_id': feed_id}  # 传入动态id
        # 发送请求并获取结果
        logging.info('用例:创业圈动态详情')
        r = base_fun.send_request(real_url, payload, user_b[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'this is a' in str(result)


if __name__ == "__main__":
    pytest.main(['2_activity_test.py'])

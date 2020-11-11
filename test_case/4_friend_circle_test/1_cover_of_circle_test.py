import pytest, allure, logging

'''
创业圈封面测试
'''


class TestCase:
    # 修改创业圈封面
    @allure.feature('修改创业圈封面')
    @pytest.mark.run(order=1)
    def test_change_cover(self, url, base_fun, user_a, cover):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param cover: 封面图片
        """
        real_url = url + '/feeds/changeCover'
        # 上传文件至oss
        base_fun.upload_file_to_oss(cover)
        payload = {'cover_image': cover[0]}  # 图片
        # 发送请求并获取结果
        logging.info('用例:修改创业圈封面')
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'success' in str(result)

    # 获取创业圈封面
    @allure.feature('获取创业圈封面')
    @pytest.mark.run(order=2)
    def test_get_cover(self, url, base_fun, user_a, change_feeds_cover):
        """
        :param url: 测试ip
        :param base_fun: 继承基类
        :param user_a: 用户A登录
        :param change_feeds_cover: 执行用例前，更换封面
        """
        real_url = url + '/feeds/cover'
        payload = {'user_id': user_a[2]}  # 用户id
        # 发送请求并获取结果
        logging.info('用例:获取创业圈封面')
        r = base_fun.send_request(real_url, payload, user_a[0])
        result = base_fun.json_loads(r.text)
        # 断言返回值
        assert 200 == r.status_code
        assert 'cover_image' in str(result)


if __name__ == '__main__':
    pytest.main('-s test_cover_of_circle.py')

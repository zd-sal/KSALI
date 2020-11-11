import requests
import json
from lib.common_fun import CommonFun
import logging
'''
封装的常用接口，如登录，发送验证码等，方便调用
'''


class BaseFun(CommonFun):
    half_url = "https://test-api.cytxoversea.com"

    def sign_in(self, area_code, phone, password):
        """
        :param area_code: 区号
        :param phone: 手机号
        :param password: 密码
        :return: 状态码，token，yunxin_id，手机号，用户id
        """
        # 生成登录地址
        url = self.half_url + "/user/login"
        # 登录数据
        payload = {'area_code': area_code, 'phone': phone, 'password': password}
        # 发送请求并获取返回值
        r = self.send_request(url, payload)
        # 状态码
        status_code = r.status_code
        # 拿到返回值
        result = json.loads(r.text)
        # 试图拿到返回值
        try:
            # 拿到token
            user_token = result['data']['token']
            # 拿到yunxin_id
            yunxin_id = result['data']['yunxin_id']
            # 拿到用户手机号
            user_phone = result['data']['phone']
            # 拿到用户id
            user_id = result['data']['id']
            return status_code, user_token, yunxin_id, user_phone, user_id
        # 排除账号不存在的报错
        except KeyError:
            self.get_verify_code(area_code, phone, '2')
            verify_code = self.make_verify_code(phone)
            self.sign_up(area_code, 'HK', phone, password, verify_code)
            # 发送注册请求，并获取返回值
            r = self.send_request(url, payload)
            status_code = r.status_code
            # 将返回值存入变量
            result = json.loads(r.text)
            # 拿到token
            user_token = result['data']['token']
            # 拿到yunxin_id
            yunxin_id = result['data']['yunxin_id']
            # 拿到用户手机号
            user_phone = result['data']['phone']
            # 拿到用户id
            user_id = result['data']['id']
            return status_code, user_token, yunxin_id, user_phone, user_id

    # 使用验证码登录
    def sign_in_by_code(self, area_code, phone, verify_code):
        """
        :param area_code: 区号
        :param phone: 手机号
        :param verify_code: 密码
        :return: 状态码，token，yunxin_id，手机号，用户id
        """
        # 获得登录地址
        url = self.half_url + "/user/login"
        # 登录数据
        payload = {'area_code': area_code, 'phone': phone, 'verify_code': verify_code}
        # 发送请求并拿到返回值
        r = self.send_request(url, payload)
        return r

    # 发送验证码
    def get_verify_code(self, area_code, phone, the_type):
        """
        :param area_code: 区号
        :param phone: 手机号
        :param the_type: type值
        :return: 返回请求值
        """
        logging.info('发送验证码')
        # 拼接地址
        url = self.half_url + "/user/sendSms"
        # 数据
        payload = {'area_code': area_code, 'phone': phone, 'type': the_type}
        # 发送请求，并获取返回值
        r = self.send_request(url, payload)
        return r

    # 验证验证码
    def verifying_the_code(self, area_code, phone, the_type, verify_code):
        """
        :param area_code: 区号
        :param phone: 手机号
        :param the_type: type值
        :param verify_code: 验证码
        :return: 请求值
        """
        logging.info('验证验证码')
        # 拼接地址
        url = self.half_url + "/user/verifyCode"
        # 数据
        payload = {'area_code': area_code, 'phone': phone, 'type': the_type, 'verify_code': verify_code}
        # 发送请求，并获取返回值
        r = self.send_request(url, payload)
        return r

    # 注册
    def sign_up(self, area_code, short_name, phone, password, verify_code):
        """
        :param area_code: 区号
        :param short_name: 区域简称
        :param phone: 手机号
        :param password: 密码
        :param verify_code: 验证码
        :return: 状态码，手机号
        """
        logging.info('注册')
        # 拼接地址
        url = self.half_url + "/user/register"
        # 数据
        payload = {'area_code': area_code, "short_name": short_name, 'phone': phone, 'password': password,
                   'verify_code': verify_code}
        # 发送请求，并获取返回值
        r = self.send_request(url, payload)
        status_code = r.status_code
        result = json.loads(r.text)
        # 将手机号传入变量
        number = result['data']['phone']
        return status_code, number

    # 退出登录
    def log_out(self, header):
        """
        :param header: 请求头
        :return: 请求结果
        """
        logging.info('退出登录')
        # 拼接地址
        url = self.half_url + "/user/signOut"
        # 发送请求，并获取返回值
        result = requests.post(url, headers=header, verify=False)
        return result

    # 删除好友
    def delete_friend(self, headers, friend_id):
        """
        :param headers: 请求头
        :param friend_id: 好友id
        :return: 请求结果
        """
        logging.info('删除好友')
        # 拼接接口地址
        url = self.half_url + "/friend/deleteFriend"
        payload = {'friend_id': friend_id}
        # 发送请求，并获取返回值
        r = self.send_request(url, payload, headers)
        return r

    # 添加好友
    def add_friend(self, header, friend_id, remark, the_type=0):
        """
        :param header: 请求头
        :param friend_id: 好友id
        :param remark: 字符串或数字
        :param the_type: type值
        :return: 请求结果
        """
        logging.info('添加好友')
        url = self.half_url + "/friend/addFriend"
        payload = {"friend_id": friend_id, "remark": remark, "type": the_type}
        # 发送请求，并获取返回值
        r = self.send_request(url, payload, header)
        return r

    # 修改用户设置
    def modify_user_setting(self, header, the_type, power=0):
        """
        :param header: 请求头
        :param the_type: type值
        :param power: 用户设置参数
        :return: 请求结果
        """
        logging.info('修改用户设置')
        url = self.half_url + "/user/setUserConfig"
        payload = {"type": the_type, 'power': power}
        # 发送请求，并获取返回值
        r = self.send_request(url, payload, header)
        return r

    # 发布动态
    def add_activity(self, header, content, share_content=None, feed_file=None, address=None, latitude=None,
                     longitude=None, the_type=1):
        """
        :param header: 请求头
        :param content: 字符串或数字内容
        :param share_content: 字典格式资讯
        :param feed_file: 图片与视频
        :param address: 地址
        :param latitude: 纬度
        :param longitude: 经度
        :param the_type: type值
        :return: 请求结果
        """
        logging.info('添加一条创业圈动态')
        # 拼接地址
        url = self.half_url + '/feeds/add'
        # 请求参数
        payload = {'content': content, 'share_content': share_content, 'feed_file': feed_file,
                   'address': address, 'feed_latitude': latitude, 'feed_longtitude': longitude, 'type': the_type}
        # 发送请求，并获取返回值
        result = self.send_request(url, payload, header)
        return result

    def delete_activity(self, header, feed_id):
        """
        :param header: 请求头
        :param feed_id: 动态id
        :return: 请求结果
        """
        logging.info('删除创业圈动态')
        # 拼接地址
        url = self.half_url + '/feeds/delete'
        # 请求参数
        payload = {'feed_id': feed_id}
        # 发送请求，并获取返回值
        r = self.send_request(url, payload, header)
        return r

    def personal_circle_list(self, header, page, user_id):
        """
        :param header: 请求头
        :param page: 页数
        :param user_id: 用户id
        :return: 请求结果
        """
        logging.info('获取个人创业圈动态列表')
        # 拼接地址
        url = self.half_url + '/feeds/userFeedList'
        # 请求参数
        payload = {'page': page, 'user_id': user_id}
        # 发送请求，并获取返回值
        r = self.send_request(url, payload, header)
        return r

    def add_friend_apply(self, headers, yunxin_id):
        """
        :param headers: 请求头
        :param yunxin_id: 云信id
        :return: 请求结果
        """
        logging.info('同意好友申请')
        # 拼接地址
        url = self.half_url + '/friend/friendApplyTry'
        payload = {'yunxin_id': yunxin_id}
        # 发送请求，并获取返回值
        r = self.send_request(url, payload, headers)
        return r


if __name__ == '__main__':
    a = BaseFun()
    r = a.sign_in('852', '53445525', '123456')
    print(r)

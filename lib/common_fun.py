import hashlib
import requests
import json
from lib.mysql_db import DB
import urllib3
import time
import os
import oss2
import random
import configparser as cparser
import math
import logging

'''
封装的公共方法，如组合header，验证手机号等
'''


class CommonFun:
    # md5加密
    @staticmethod
    def encrypting(string):
        """
        :param string: 传入字符串
        :return: 传回md5加密后的值
        """
        r = hashlib.md5(string.encode()).hexdigest()
        return r

    # 获取绝对路径
    @staticmethod
    def base_dir():
        """
        :return:返回绝对路径
        """
        base_dir = str(os.path.dirname((os.path.dirname(__file__))))
        # 替换换行符
        base_dir = base_dir.replace('\\', '/')
        return base_dir

    # 拼接header
    def header(self, token=None):
        """
        :param token: 传入token值
        :return: 返回header
        """
        # 文件名
        file = 'header_config.ini'
        # keywords
        key_list = ['User-Agent', 'Content-Type', 'Host', 'Connection', 'Accept-Encoding']
        # 读取配置文件，得到字典
        data = self.read_ini(file, key_list)
        # 拼接header
        headers = {'User-Agent': data['User-Agent'],
                   'Content-Type': data['Content-Type'],
                   'Host': data['Host'],
                   'Connection': data['Connection'],
                   'Accept-Encoding': data['Accept-Encoding'],
                   'token': token
                   }
        # 无token
        if token is None:
            headers.pop('token')
            return headers
        # 有token
        else:
            return headers

    # 封装的发送请求
    def send_request(self, url, payload={}, headers=None):
        """
        :param url: 传入接口地址
        :param payload: 传入请求数据
        :param headers: 传入请求头
        :return: 返回请求结果
        """
        if headers is None:
            headers = self.header()
        # 处理警告
        urllib3.disable_warnings()
        # 发送请求
        result = requests.post(url, data=payload, headers=headers, verify=False)
        return result

    # 创建手机号
    @staticmethod
    def create_phone():
        """
        :return: 返回符合手机号格式的数字
        """
        logging.info('创建手机号')
        # 选择9或6为第一个数
        while True:
            # 生成第一个数
            first = [6, 9][random.randint(0, 1)]
            # 生成第二个数
            second = [1, 2, 3, 4, 5, 7, 8][random.randint(0, 5)]
            # 合并前两个数
            merge1 = "{}{}".format(first, second)
            # 创建字符串拼接第三第四个数
            merge2 = ''
            for j in range(0, 2):
                merge2 = merge2 + str(random.randint(0, 7))
            merge2 = merge2
            # 前两个数不可等于第三和四个数
            if merge1 != merge2:
                # 创建后四位数
                suffix = random.sample(range(0, 9), 4)
                suffix = "{}{}{}{}".format(suffix[0], suffix[1], suffix[2], suffix[3])
                # 拼接出手机号
                phone = "{}{}{}".format(merge1, merge2, suffix)
                return phone
            else:
                continue

    # 在数据库中验证手机号码是否已被注册
    @staticmethod
    def verify_it_in_db(phone):
        """
        :param phone: 传入数字
        :return: 在数据库中查验的结果
        """
        logging.info('数据库中验证')
        db = DB()
        # 在数据库中搜索该手机号
        result = db.select_sql(phone)
        # 关闭数据库
        db.close()
        return result

    # # 创建多个手机号
    # def create_multiple_phone(self, how_many_you_want=1):
    #     # 数据只能为int
    #     if type(how_many_you_want) != int:
    #         how_many_you_want = 1
    #     # 最大只生成10个随机手机号
    #     elif how_many_you_want > 10:
    #         how_many_you_want = 10
    #     # 创建用于添加手机号的列表
    #     num_list = []
    #     n = 0
    #     while n == 0:
    #         # 创建手机号
    #         phone = self.create_phone()
    #         # 在数据库中验证
    #         result = self.verify_it_in_db(phone)
    #         # 判定手机号是否在列表中
    #         if result == 0 and phone not in num_list:
    #             num_list.append(phone)
    #             # 判断数量是否已经达到输入量
    #             if len(num_list) == how_many_you_want:
    #                 # 返回列表
    #                 return num_list
    #         else:
    #             continue

    # 封装的json方法
    @staticmethod
    def json_loads(params):
        """
        :param params: 传入json格式字符串
        :return: 返回转换后的值
        """
        r = json.loads(params)
        return r

    @staticmethod
    def json_dumps(params):
        """
        :param params: 传入多种类型值
        :return: json编码后的字符串
        """
        r = json.dumps(params, ensure_ascii=False)
        return r

    # 时间戳
    @staticmethod
    def time_stamp():
        """
        :return: 返回时间戳
        """
        stamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        return stamp

    # 在测试数据中选择一张图片或视频
    def pic_vid(self, pic_or_vid=1):
        """
        :param pic_or_vid: 传入数字或字符串
        :return: 图片或视频
        """
        # 拿到绝对路径
        base_dir = self.base_dir()
        # 生成一个空列表
        file_names = []
        if type(pic_or_vid) == int:
            path = base_dir + '/test_data/pic'
        else:
            path = base_dir + '/test_data/video'
            pic_or_vid = 1
        all_files = os.listdir(path)
        for i in range(pic_or_vid):
            # 在图片数量内，产生随机数，并返回多个图片
            number = random.randint(0, len(all_files) - 1)
            # 选择对应的图片
            file_name = all_files[number]
            # 存入列表
            file_names.append(file_name)
        return file_names

    # 图片或视频发送动态
    def pic_and_vid(self, number=1):
        """
        :param number: 需要的图片数量
        :return: 动态图片名称，oss字典
        """
        base_dir = self.base_dir()
        if type(number) != int:
            number = 'dfa'
            path = '/test_data/video/'
            oss_path = 'video/'
        else:
            path = '/test_data/pic/'
            oss_path = 'circle/'
        # 选定图片
        files = self.pic_vid(number)
        # 创建列表接收文件名
        all_file = []
        # 创建字典用于上传oss
        oss_dic = {}
        i = 0
        # 在图片列表中循环拼接
        for file in files:
            # 拼接图片路径
            file_path = base_dir + path + file
            # 拼接图片名
            file_name = oss_path + file
            # 图片放入列表
            all_file.append(file_name)
            # 路径和文件名放入字典
            oss_dic[str(i)] = [file_name, file_path]
            i += 1
        # 将列表转为json文件
        file_list = self.json_dumps(all_file)
        number = len(all_file)
        return file_list, oss_dic, number

    # 图片或视频发送动态
    def headimg_cover(self, head_or_cover='cover'):
        """
        :param head_or_cover: 需要的图片类型
        :return: 图片名称，oss字典
        """
        path = '/test_data/pic/'
        base_dir = self.base_dir()
        if head_or_cover == 'cover':
            oss_path = 'cover/'
        else:
            oss_path = 'head_img/'
        # 选定图片
        files = self.pic_vid()
        # 创建列表接收文件名
        all_file = []
        # 创建字典用于上传oss
        oss_dic = {}
        i = 0
        # 在图片列表中循环拼接
        for file in files:
            # 拼接图片路径
            file_path = base_dir + path + file
            # 拼接图片名
            file_name = oss_path + file
            # 图片放入列表
            all_file.append(file_name)
            # 路径和文件名放入字典
            oss_dic[str(i)] = [file_name, file_path]
            i += 1
        return file_name, oss_dic, 1

    def upload_file_to_oss(self, pic):
        """
        :param pic: 文件名,文件路径
        """
        # 读取配置文件
        logging.info('上传文件至oss')
        file = 'oss_config.ini'
        # 关键词
        keys = ['end_point', 'key_id', 'key_secret', 'bucket_name']
        # 读取文件key对应值
        data = self.read_ini(file, keys)
        # 传入endpoint
        endpoint = data['end_point']
        # 阿里云RAM账号AccessKey登入oss
        auth = oss2.Auth(data['key_id'], data['key_secret'])
        # 连接Bucket
        bucket = oss2.Bucket(auth, endpoint, data['bucket_name'], connect_timeout=30)
        # 上传文件
        for i in range(0, pic[2]):
            bucket.put_object_from_file(pic[1][str(i)][0], pic[1][str(i)][1])

    # 读取ini文件
    def read_ini(self, file_path, element):
        """
        :param file_path: 文件路径
        :param element: keyword列表
        :return: keyword与value的字典
        """
        # 拼接ini文件路径
        path = self.base_dir() + '/configure/' + file_path
        cf = cparser.ConfigParser()
        cf.read(path)
        # 获取section名
        section = cf.sections()
        elements = {}
        # 从列表中拿出keyword
        for i in element:
            # 将keyword对应的数据拿出来
            string = cf.get(section[0], i)
            # 将key和数据存入字典
            elements[i] = string
        return elements

    # 创建用户数据
    def make_user(self):
        """
        :return: 用户参数
        """
        # 文件路径
        file = 'user_config.ini'
        # keyword
        keys = ['A', 'B', 'area_code', 'short_name', 'password']
        # 读取ini中的数据，并得到字典
        data = self.read_ini(file, keys)
        return data

    # 这里的参数包括一个基准点，和一个距离基准点的距离
    def position(self):
        """
        :return: 地址及经纬度
        """
        logging.info('生成地址')
        # 文件路径
        file = 'location_config.ini'
        # keyword列表
        elements = ['ak', 'longitude', 'latitude', 'radius', 'url']
        # 读取文件
        data = self.read_ini(file, elements)
        # 随机生成位置偏移
        radius_in_degrees = int(data['radius']) / 111300
        u = float(random.uniform(0.0, 1.0))
        v = float(random.uniform(0.0, 1.0))
        w = radius_in_degrees * math.sqrt(u)
        t = 2 * math.pi * v
        x = w * math.cos(t)
        y = w * math.sin(t)
        # 位置起点加偏移生成经纬度
        longitude = y + float(data['longitude'])
        latitude = x + float(data['latitude'])
        # 这里是想保留6位小数点
        loga = '%.6f' % longitude
        lata = '%.6f' % latitude
        # 拼接经纬度为字符串
        lata_loga = lata + ',' + loga
        # 拼接百度地图api地址
        url = data['url'].format(data['ak'], lata_loga)
        # 发送get请求
        r = requests.get(url)
        result = self.json_loads(r.text)
        return lata, loga, result['result']['formatted_address']


if __name__ == '__main__':
    c = CommonFun()
    phone = '12345678'

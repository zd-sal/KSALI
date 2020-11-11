import pymysql
from pymysql.err import OperationalError
import os
import configparser as cparser

'''
封装数据库操作，用于查询手机号是否已经注册
'''

# -------------------------------------读取db_config.ini-------------------------------------------------------
# 绝对路径
base_dir = str(os.path.dirname((os.path.dirname(__file__))))
base_dir = base_dir.replace('\\', '/')
# 配置文件路径
file_path = base_dir + '/configure/db_config.ini'
cf = cparser.ConfigParser()
cf.read(file_path)
section = cf.sections()[0]
# 从ini文件读取数据库参数
host = cf.get(section, 'host')
port = cf.get(section, 'port')
db = cf.get(section, 'db_name')
user = cf.get(section, 'user')
password = cf.get(section, 'password')


# =============================封装MYsql基本操作=========================================================
class DB:
    # 连接数据库
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=host,
                                        user=user,
                                        password=password,
                                        db=db,
                                        port=int(port))
        # 排除连接错误
        except OperationalError as e:
            print('Mysql Error %d: %s' % (e.args[0], e.args[1]))

    # 在数据库中查找手机号
    def select_sql(self, num):
        """
        :param num: 数字
        :return: 查验结果
        """
        real_sql = 'select * from cytx_user_login_info where phone = ' + num + ';'
        with self.conn.cursor() as cursor:
            # 执行sql语句
            r = cursor.execute(real_sql)
        self.conn.commit()
        return r

    # 关闭数据库
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    pass

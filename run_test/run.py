# -*- coding:utf-8 -*-
import os, pytest, sys
import logging

base_dir = str(os.path.dirname((os.path.dirname(__file__))))
direction = base_dir + '\\allure-2.13.6\\bin\\'
sys.path.append(direction)
sys.path.append(base_dir)
from lib.common_fun import CommonFun

time_stamp = CommonFun.time_stamp()
"""
执行用例页面
"""


# 执行

def log():
    """
    :return: 返回log
    """
    # log日志输出格式
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # log文件位置
    logfile = '../report/log/' + time_stamp + '.txt'
    logger = logging.getLogger()
    # log级别
    logger.setLevel(logging.INFO)
    # log输出至文件
    fh = logging.FileHandler(filename=logfile, mode='w', encoding='utf-8')
    # log输出至console
    ch = logging.StreamHandler()
    # 设置log日志文件格式
    fh.setFormatter(formatter)
    # 设置log日志console格式
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


def report(style: list):
    """
    :param style: 传入pytest执行参数
    """
    logger = log()
    logger.info('Start')
    # 文件路径
    path_allure = '../report/allure/' + time_stamp + '/xml'
    path_html = '../report/allure/' + time_stamp + '/html'
    # 生成allure报告
    pytest.main(style + ['--alluredir={path_allure}'.format(path_allure=path_allure)])
    # 生成HTML报告
    os.system('allure generate {path_allure} -o {path_html} --clean'
              .format(path_allure=path_allure, path_html=path_html))
    # 开启allure web服务
    # os.system('allure open {path_html}'.format(path_html=path_html))
    logger.info('End')


if __name__ == '__main__':
    direction = base_dir
    style0 = ['-s', '-q', direction, '--reruns', '3', '--reruns-delay', '5']
    # style0 = ['-s', '-q', direction]
    report(style=style0)

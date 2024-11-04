"""
Author: Wyatt1026
Project Address: https://github.com/Wyatt1026/BilibiliDailyUp
"""


from core.bilibili import Bilibili
from config import config
from os import environ
import random

if __name__ == '__main__':
    ck_list = config.COOKIE_LIST
    # for ck in ck_list:
    ck = random.choice(ck_list)
    # 获取指定用户的视频列表，mid 为用户id
    # 修改mid即可获取该用户的 bvids 列表
    bilibili = Bilibili(ck)
    # 去看剧
    # mid = '3546766586678158'
    # 白色苹果冻
    mid = '1794984662'
    # litscorpi
    # mid = '431316421'
    count = 30
    bvids_list = bilibili.user_video_list(mid, count)
    print(bvids_list)

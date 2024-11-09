"""
Author: Wyatt1026
Project Address: https://github.com/Wyatt1026/BilibiliDailyUp
"""


from core.bilibili import Bilibili
from config import config
import os
import datetime

if __name__ == '__main__':
    cookies = os.environ.get('COOKIES')
    ck_list = cookies.split(",")

    # 构造mid列表
    def mid_list(list):
        return [item['mid'] for item in list]
    # 构造用户列表
    def uname_list(list):
        return [item['uname'] for item in list]
    
    # 要修改日期
    # 筛选关注日期小于2024-11-01的数据，默认取关没有互粉且非特别关注，没有加入任何组的用户
    relation_date_str = '2024-11-1'
    
    # 多用户要注意选取对应uid的CK值
    ck = ck_list[4]
    bilibili = Bilibili(ck)
    user_data = bilibili.test_info()
    mid = user_data.get('mid')
    username = user_data.get('name', '未知')
   
    list = bilibili.relation_list_all(mid)
    username =bilibili.test_info()
    # print(list)
    print(f'{username}共关注了{len(list)}个用户')
    # print(mid_list(list))
    # print(uname_list(list))

    
    # 将日期字符串转换为 datetime 对象
    relation_date = datetime.datetime.strptime(relation_date_str, '%Y-%m-%d')
    # 将 datetime 对象转换为时间戳
    timestamp = int(relation_date.timestamp())
    # print(timestamp)
    quguan_list = [item for item in list if item['mtime'] < timestamp]
    # print(mid_list(quguan_list))

    # 筛选标签为空的数据
    n_list = [item for item in quguan_list if item['tag'] == None]
    # print(mid_list(n_list))

    # 筛选非特别关注的数据
    unspecial_list = [item for item in n_list if item['special'] == 0]
    # print(mid_list(unspecial_list))

    # 筛选没有互粉的数据
    unfollow_list = [item for item in unspecial_list if item['attribute'] != 6]
    # print(unfollow_list)
    print(f'{relation_date_str}以前,{username}共有{len(unfollow_list)}个用户没有互粉')
    # print(mid_list(unfollow_list))
    
    
    print('取关列表：')
    un_mid_list = mid_list(unfollow_list)
    print(uname_list(unfollow_list))


   
    # 取关
    for un_mid in un_mid_list:

        # print(f'{username}取关{un_mid}')
        bilibili.relation_unfollow(un_mid)

    print('取关结束')
   
        
    

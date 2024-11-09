"""
the api for bilibili
"""

from enum import Enum


class Api(Enum):
    nav_url = 'https://api.bilibili.com/x/web-interface/nav'
    info_url = 'http://api.bilibili.com/x/space/myinfo'
    coin_url = 'http://account.bilibili.com/site/getCoin'
    inquire_url = 'https://api.bilibili.com/x/member/web/exp/reward'
    get_video_list_url = 'https://api.bilibili.com/x/space/wbi/arc/search?{}'
    watch_video_url = 'https://api.bilibili.com/x/click-interface/web/heartbeat'
    share_video_url = 'https://api.bilibili.com/x/web-interface/share/add'
    insert_coins_url = 'https://api.bilibili.com/x/web-interface/coin/add'
    live_sign_url = 'https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign'
    live_info_url = 'https://api.live.bilibili.com/xlive/web-ucenter/user/get_user_info'
    silver_to_coin_url = 'https://api.live.bilibili.com/xlive/revenue/v1/wallet/silver2coin'
    comics_sign_url = 'https://manga.bilibili.com/twirp/activity.v1.Activity/ClockIn'
    comics_check_url = "https://manga.bilibili.com/twirp/activity.v1.Activity/GetClockInInfo"
    VIDEO_INFO = "https://api.bilibili.com/x/web-interface/view"
    watch_video_click_url = 'https://api.bilibili.com/x/click-interface/click/web/h5'
    click_like_url = 'https://api.bilibili.com/x/web-interface/archive/like'
    shoucang_url = 'https://api.bilibili.com/x/v3/fav/resource/deal'
    sanlian_url = 'https://api.bilibili.com/x/web-interface/archive/like/triple'
    reply_url = 'https://api.bilibili.com/x/v2/reply/add'
    relation_url = 'https://api.bilibili.com/x/relation/followings'
    relation_modify_url = 'https://api.bilibili.com/x/relation/modify'


"""
The config for this script, you can read the description in README.md
"""

LIKE_OR_NOT = True
# 投币时是否点赞

USE_ENVIRONMENT_VARIABLE = False
# 从环境变量中读取CK 确保已经设置环境变量BILIBILI 只支持单个账号

COIN_OR_NOT = True
# 是否投币

COIN_NUM = 1
# 投币数量 -1为完成所有也就是如果你已经投过1次那就只会投4次
# 如果不是 -1 则指定投币数量范围1-5

SILVER2COIN_OR_NOT = True
# 是否将银瓜子兑换为硬币


STRICT_MODE = True
# 是否开启严格模式，严格模式会保证至少5次成功投币，因为官方投币API存在缺陷，会有投币成功但是返回失败的情况
# 默认开启严格模式，如果关闭则只会投币5次，无论成功失败，会出现少投币的情况，因为可能失败，但是不会造成浪费硬币的情况，自行选择
NUM_MODE = False
# 该模式与严格模式互斥,开启此模式,投币只会投COIN_NUM次,无论成功失败

UID_LIST = ['431316421', '3546766586678158', '1794984662']
# 投币UP主的ID号,如果不修改，默认将用上面这个列表里的,可以选择自己喜欢的UP主
# 获取UID的方法见README.md
# 新华网 人民日报 央视频  王冰冰 英雄联盟赛事

COOKIE_LIST = [
    r"buvid4=E6743522-0A8B-B259-D470-C94F871D497832277-022012015-8XWAWYnEgRUvVI4nIgt5cw%3D%3D; LIVE_BUVID=AUTO8316521815636669; buvid_fp=5dff3c6f6041b851c39f4f4a2313c9d6; PVID=1; rpdid=|(u))lk||l|k0J'uYYm|u|m|u; buvid3=41A98AD8-BAA9-422F-8588-0113E4C4734B148821infoc; CURRENT_FNVAL=4048; header_theme_version=CLOSE; browser_resolution=1920-975; home_feed_column=5; b_nut=100; _uuid=89109A11010-8F27-66EF-1B61-41FF10E34238941624infoc; enable_web_push=DISABLE; DedeUserID=1794984662; DedeUserID__ckMd5=ff00be248f5441ef; SESSDATA=d1e2c85c%2C1746183781%2C2c40c%2Ab2CjAFaKcfrEQMJTsY_3AHq7l5vmVk0uvgmWMZi707jCKuHr9LiEv3a0zANSKwqRrJHkYSVkpua0lPbjRIRjNfU2F6OFZFZDdVS3QwdnRJUm5EeGtrZnowRHpGblRtd1FjbTVjTmdhTzVyLW1oY2dxRjN2d29QQzBqV1JzWW1WVklVb2lSZTFKYmZRIIEC; bili_jct=70ee100d91fabb6ede7d003374b46499; sid=fjsx2571; bp_t_offset_1794984662=995822827963678720; b_lsid=DFF9294F_19305ADEC3B; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzEyMjYzMTAsImlhdCI6MTczMDk2NzA1MCwicGx0IjotMX0.A8zvLex_CvPpg2RbblAYbKsxap32WdHXqXc9fl_1mdI; bili_ticket_expires=1731226250",r"buvid4=D6BE84FC-EFB5-B0E1-48E0-010BC117BE3A91548-022051019-mDP2PkqgyTnYK/y30/SOcEpImGDEOj79riq0JsmgGOhcAgbf+13X7g%3D%3D; buvid_fp=03d2da5557211f35ca5d7b29319f008c; LIVE_BUVID=AUTO3916521821213374; buvid3=8F3BA39C-D906-98C1-3D06-BC67E15A135B79953infoc; b_nut=1727104779; _uuid=191099AD6-BC17-2E7C-910F8-49F9DEE64F4F81146infoc; enable_web_push=DISABLE; DedeUserID=3546766586678158; DedeUserID__ckMd5=311e687f25e3b9b5; header_theme_version=CLOSE; home_feed_column=5; browser_resolution=1920-975; CURRENT_FNVAL=4048; rpdid=0zbfvSbQGu|HK7Zj2H3|3FB|3w1SSPIC; dy_spec_agreed=1; hit-dyn-v2=1; bp_t_offset_3546766586678158=994890837240315904; SESSDATA=844ced14%2C1746183490%2Cc49de%2Ab2CjCipMc1Drsv6jU9fBMuOe27mOqJs6a-0CX3IdEYn-FZ5xI3sBp0h5y43i9aepwm7P8SVl9WLWxVMVZMdkpBUExHcnRSU0h5MFpsTjhYT0NMalBBY1BDTzBJaXdJb2dYaHpocGh4TXFjS0REVkxXZ25JdnNwWFpTQnVuWWhPYjBRRUFBQ094LWFRIIEC; bili_jct=58789ce04e2fe829f21cfb1936b4aa37; sid=6v7bwh2o; b_lsid=E1048610EA_19305AF90CD",r"buvid3=10879112-092E-AC02-E3E1-727C505B208D98619infoc; b_nut=1727862298; _uuid=12F63F68-D1078-71075-36FD-8685D7DE753699400infoc; enable_web_push=DISABLE; buvid4=96E59510-68D8-BE3F-23D6-F93CBA76DD9602285-024100209-xBCrltfYy0zks+MDWCytQutrofaTRg3Pzh/ITb6sR37FxMTLR+u91LRwLoonC68v; buvid_fp=dfe12467d3b82339c01923765a568f89; header_theme_version=CLOSE; DedeUserID=3546776470555432; DedeUserID__ckMd5=93636570af93a5ee; CURRENT_FNVAL=4048; rpdid=0zbfvSbQGu|qxp9hzR0|vO8|3w1T0i3g; CURRENT_QUALITY=80; bp_t_offset_3546776470555432=988118541397917696; b_lsid=5CEEC5610_192E5BC7E36; SESSDATA=bc2662c4%2C1745983194%2Ca6835%2Ab1CjDLOT-7p77q-YLu1omD2YkqFHbuBYgxPhhyHgxaZgyMlzKI7v6Dyga_np1RCIz9wHUSVjN4Wno0cm9FZEpaMlExQ1l3eXFXZ2dwcDRNM0N0QzZRM2hUMVo0dm9YemdrSWxsZGR4Uk1HTml1M2NWUmp1dGFwajl2aUlUV0lwazc2SGRsWVpiRWR3IIEC; bili_jct=7344dc4e19b6fd2ee623033635237300; sid=pt5ytlgk; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA2OTAzOTgsImlhdCI6MTczMDQzMTEzOCwicGx0IjotMX0.oPGWyNx7rgTaR6ul4Dj9tpaTGOBbKlHff_-IhhyU34Y; bili_ticket_expires=1730690338; home_feed_column=4; browser_resolution=400-888",r"buvid3=35264C13-CFB2-DE38-C44A-F54D3C5C916610134infoc; b_nut=1728960610; _uuid=9C45FEAE-E5A3-8E12-F62A-E3833E519E10410765infoc; enable_web_push=DISABLE; buvid4=963F0DC0-0AB6-6A0F-26B0-B3BAEB3EB9C911538-024101502-pTl/QoSssHMwHTofBBTPX9jnzcD5LppC+eKteDDBvQMpv2UQ417hO0dZBXyQn9vz; buvid_fp=8741fd7b610676e58a7b650b22553b7a; DedeUserID=3546777600919923; DedeUserID__ckMd5=52f8c8280d7b52ac; header_theme_version=CLOSE; CURRENT_FNVAL=4048; home_feed_column=5; rpdid=0zbfvSbQGu|qxpYJV8m|2kf|3w1T0yl1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjk0Nzc1MzksImlhdCI6MTcyOTIxODI3OSwicGx0IjotMX0.zlyV3RZw3Mdo4FBeDjNANC_67wRqfThL0qXCopeEM0o; bili_ticket_expires=1729477479; SESSDATA=0eec1500%2C1744772199%2C4e320%2Aa1CjAcaWryw0yCzGU4OpY_X7vRWXwKzB-n9f9b5ZWiubnHq1Dpz_9q5vhkwVfxSGrEVrUSVnV1YlE4bGFTWTlYdzdkaUtZSUE5ZmlERHJzdlduYjJtQjB1MlZPQU5Rb2tONGlaaXlHdF9VOXRub2pWalRmOWFLRldPdGNsbjViZnpNNHBLUDRneW9nIIEC; bili_jct=d7417ad7f00061cf4b77ee277319ed57; sid=8vbo0khc; b_lsid=1010BB394D_192ACD2896C; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bp_t_offset_3546777600919923=990582521185959936; browser_resolution=1777-1435",r"buvid3=CE2377CA-4AAC-BAC4-26EC-B8A500E4E14F99456infoc; b_nut=1700388599; _uuid=6DE63C46-D1C6-82FA-9FFA-245D4C26F35901542infoc; buvid4=DEF12488-B407-A867-6A08-522DEBD53CF200856-023111910-; rpdid=0zbfvSbQKG|aPWrcnwb|KZ4|3w1R4EKL; user_device_id=a969efb39cbc4ec5a671f08a3ba4b932; user_device_id_timestamp=1703166973963; DedeUserID=431316421; DedeUserID__ckMd5=8a4b6a7508bfcfca; buvid_fp_plain=undefined; hit-dyn-v2=1; header_theme_version=CLOSE; enable_web_push=DISABLE; home_feed_column=5; CURRENT_BLACKGAP=0; browser_resolution=1872-966; CURRENT_QUALITY=80; LIVE_BUVID=AUTO6317290025914441; CURRENT_FNVAL=4048; bp_t_offset_431316421=995957728591478784; fingerprint=750ef6d91354fb33673e9925db6003c7; buvid_fp=750ef6d91354fb33673e9925db6003c7; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzExOTYwMzUsImlhdCI6MTczMDkzNjc3NSwicGx0IjotMX0.fy5BHa5zA0o9gY-kRvw5Cb19dETK1M3A8dIyL34LlR8; bili_ticket_expires=1731195975; SESSDATA=43704b03%2C1746488838%2Cd014c%2Ab1CjCvZHQTvaK9DsFEqfe6kPrkgiXq0VtqToZS1Nb0f59SxmyekZOIa_DujFfeYc68SdUSVjVQSER2cGkxdXB0c1ZHc1RYRmN3WjRNNnhrNkh0a1A0V0Z3TUU2T0tKWnNGRzVmRVF1Tno2cTdwVVh5RFIxY0x6ZFpJSjdUMXNUUkVqeXVwT1BDMXVnIIEC; bili_jct=c7e81655d7a29e4c2e9c3fdf4eea8689; sid=56ycvtq9; b_lsid=3E44C6F8_19305AB8309"
]
# Bilibili的COOKIE获取的方法见README.md 支持多账号

PUSH_OR_NOT = False
TOKEN = ''
# PUSH PLUS的TOKEN 官网为https://www.pushplus.plus

WECHAT_PUST_OR_NOT = True
# 默认关闭企业微信推送

WECHAT_ID = "wwf8996175e40b25ac"
# 企业ID
WECHAT_SECRET = "cUzqXTv-ycuxUkGoqUFoi3HLLo9Xd50GNPmKtC1lxLM"
# 企业应用secret
WECHAT_APP_ID = "1000002"
# 企业应用的id
# 企业应用推送 文档https://developer.work.weixin.qq.com/document/path/90236

SERVER_PUSH_OR_NOT = False
SERVER_KEY = ""
# 是否开启sever酱,有填写则推送,空字符串则不推送 https://sct.ftqq.com/sendkey获取key

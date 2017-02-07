#-*- coding:utf-8 -*-
import xadmin

from .models import EmailVerifyRecord,Banner

class EmailVerifyRecordAdmin(object):
    list_display=[
        'code','email','send_type','send_time'
    ]#页面列表中显示哪些字段
    search_fields=[
        'code','email','send_type'
    ]#定义页面搜索栏
    list_filter=[
        'code','email','send_type','send_time'
    ]

class BannerAdmin(object):
    pass


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)


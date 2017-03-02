#-*- coding:utf-8 -*-
import xadmin
from xadmin import views

from .models import EmailVerifyRecord,Banner

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSetting(object):
    site_title="我的测试后台"
    site_footer="right by simba"
    menu_style="accordion"


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
    list_display=['title','image','url','index','add_time']
    search_fields=['title','image','url','index']
    list_filter=['title','image','url','index','add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
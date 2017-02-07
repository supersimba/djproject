#coding:utf-8
#
import xadmin

from .models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):
    list_display=['name','desc','detail','degree','learn_times','students',
                      'fav_nums','image','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'students']
    list_filter = ['name','desc','detail','degree','learn_times','students',
                      'fav_nums','image','click_nums']

class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course','name','add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
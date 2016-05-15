#encoding:utf8
import xadmin
from .models import *
from plugins import FilterOwnedItems,AddOwnerPlugin
from xadmin.views import ListAdminView,ModelFormAdminView
from xadmin.plugins.auth import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class UserInline(object):
    model=Employee
    fk_name='user'
class UserAdmin(BaseUserAdmin):
    only_view_owned=True

class EmployeeAdmin(object):
    only_view_owned=True
    list_display=('name','tel','qq','owner','address')
    list_display_links=('name',)
    search_fields=['name','tel','qq','address','owner']

class ClientAdmin(object):
    only_view_owned=True
    list_display=('name','tel','qq','address')
    list_display_links=('name')
    search_fields=['name','tel','qq','address']
class PublicArticleAdmin(object):
    only_view_owned=True
    pass
class WriteArticleAdmin(object):
    only_view_owned=True
    pass





xadmin.site.register_plugin(FilterOwnedItems,ListAdminView)
xadmin.site.register_plugin(AddOwnerPlugin,ModelFormAdminView)


xadmin.site.register(Client,ClientAdmin)
xadmin.site.register(PublicArticle,PublicArticleAdmin)
xadmin.site.register(WriteArticle,WriteArticleAdmin)
xadmin.site.unregister(User)
xadmin.site.register(User,UserAdmin)
xadmin.site.register(Employee,EmployeeAdmin)

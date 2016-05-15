#encoding:utf8
from xadmin.views import BaseAdminPlugin
from django.contrib.auth.models import User
from django.db.models import Q
from models import *
class FilterOwnedItems(BaseAdminPlugin):
    only_view_owned=False
    def init_request(self,*args,**kwargs):
        return bool(self.only_view_owned)

    def get_list_queryset(self,queryset):
        if self.user.is_superuser:
            return queryset
        av=self.admin_view
        if av.model==User:
            q=queryset.filter(Q(pk__in=self.user.members.values_list('user_id')) | Q(pk=self.user.id))
        else:
            q=queryset.filter(Q(owner__in=self.user.members.values_list('user_id')) | Q(owner=self.user))
        return q

class AddOwnerPlugin(BaseAdminPlugin):
    def init_request(self,*args,**kwargs):
        av=self.admin_view

        return av.model in [Employee,Client,PublicArticle,WriteArticle]
    def save_forms(self):
        if hasattr(self.admin_view.new_obj,'owner')\
         and self.admin_view.new_obj.owner is None:
            self.admin_view.new_obj.owner=self.user
#encoding:utf8
from django.db import models
from django.conf import settings


# Create your models here.

class Employee(models.Model):
    class Meta:
        verbose_name=u'用户信息'
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=u'管理员', \
        blank=True,related_name='members',null=True, \
        help_text=u'改位置可以留空，也可以给改员工添加管理员，这样管理员可以查看该员工的所有信息。')
    user=models.OneToOneField(settings.AUTH_USER_MODEL,related_name='profile',verbose_name=u'登录用户', \
        help_text=u'如果允许该员工登录管理平台，需要在这里给他添加账户')
    name=models.CharField(max_length=20,verbose_name=u'姓名')
    tel=models.IntegerField(verbose_name=u'电话')
    qq=models.IntegerField(verbose_name=u'QQ')
    more=models.TextField(verbose_name=u'备注')
    address=models.CharField(max_length=100,verbose_name=u'地址')
    def __unicode__(self):
        return self.name

class Client(models.Model):
    class Meta:
        verbose_name=u'客户'
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,\
        verbose_name=u'所属用户',
        help_text=u'如果留空，默认为登录用户，也可以填写一名员工，这样该员工就可以查看该客户的信息。')
    name=models.CharField(max_length=20,verbose_name=u'姓名')
    tel=models.IntegerField(verbose_name=u'电话')
    qq=models.IntegerField(verbose_name=u'QQ')
    more=models.TextField(verbose_name=u'备注')
    address=models.CharField(max_length=100,verbose_name=u'地址')
    def __unicode__(self):
        return self.name


class PublicArticle(models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,\
        verbose_name=u'接单人',\
        help_text=u'如果留空，默认为登录用户，也可以设定一名员工，表明是该员工接单' )
    ArticleKinds={1:u'普刊',2:u'核心',3:u'学报',4:u'专利',5:u'其他'}
    Banks={1:u'建行',2:u'工行',3:u'支付宝',4:u'微信'}
    Status={1:u'未完成',2:u'完成'}
    class Meta:
        verbose_name=u'采编信息'
    kind=models.IntegerField(choices=ArticleKinds.items(),verbose_name=u'类型')
    author=models.ForeignKey('Client',verbose_name=u'作者')
    journal=models.CharField(max_length=100,verbose_name=u'刊物')
    periodical=models.CharField(max_length=20,verbose_name=u'期次')
    title=models.CharField(max_length=100,verbose_name=u'题目')
    totalmoney=models.FloatField(verbose_name=u'总金额')
    deposit=models.FloatField(verbose_name=u'定金')
    rest=models.FloatField(verbose_name=u'余额')
    resttime=models.DateField(verbose_name=u'余额到款时间')
    bank=models.IntegerField(verbose_name=u'到款银行',choices=Banks.items())
    more=models.TextField(verbose_name=u'员工备注')
    status=models.IntegerField(verbose_name=u'状态',choices=Status.items(),default=1)
    def __unicode__(self):
        return str(self.author) + self.title

class WriteArticle(models.Model):
    ArticleKinds={1:u'普通论文',2:u'研究生论文',3:u'核心',4:u'其他'}
    Banks={1:u'建行',2:u'工行',3:u'支付宝',4:u'微信'}
    Status={1:u'未完成',2:u'修改中',3:u'完成',4:u'黄稿'}
    class Meta:
        verbose_name=u'代写信息'
    kind=models.IntegerField(choices=ArticleKinds.items(),verbose_name=u'类型')
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=u'接单人',blank=True,null=True,\
        help_text=u'如果留空，默认为登录用户，也可以设定一名员工，表明是该员工接单' )
    client=models.ForeignKey('Client',verbose_name=u'下单人')
    title=models.CharField(max_length=100,verbose_name=u'题目')
    wordcount=models.IntegerField(verbose_name=u'字数')
    perword=models.FloatField(verbose_name=u'单价（千字）')
    totalmoney=models.FloatField(verbose_name=u'总金额')
    deposit=models.FloatField(verbose_name=u'定金')
    rest=models.FloatField(verbose_name=u'余额')
    finishtime=models.DateField(verbose_name=u'交稿时间')
    bank=models.IntegerField(verbose_name=u'到款银行',choices=Banks.items())
    more=models.TextField(verbose_name=u'员工备注')
    status=models.IntegerField(verbose_name=u'状态',choices=Status.items(),default=1)
    def __unicode__(self):
        return str(self.client) + self.title

    
__all__=['Client','PublicArticle','WriteArticle','Employee']
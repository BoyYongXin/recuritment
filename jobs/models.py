from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.
# 候选人学历
DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))

JobTypes = [
    (0,"技术类"),
    (1,"产品类"),
    (2,"运营类"),
    (3,"设计类"),
    (4,"市场营销类")
]

Cities = [
    (0,"北京"),
    (1,"上海"),
    (2,"深圳"),
    (3,"杭州"),
    (4,"广州")
]

class Job(models.Model):
    # Translators: 职位实体的翻译
    """
    SmallIntegerField int类型
    blank=False,不可以为空
    default=默认值
    """
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name=_("职位类别"))
    job_name = models.CharField(max_length=250, blank=False, verbose_name=_("职位名称"))
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name=_("工作地点"))
    job_responsibility = models.TextField(max_length=1024, verbose_name=_("职位职责"))
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name=_("职位要求"))
    creator = models.ForeignKey(User, verbose_name=_("创建人"), null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name=_("创建日期"), auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name=_("修改日期"), auto_now=True)
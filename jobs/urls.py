from django.conf.urls import url
from django.urls import path
from django.conf import settings

from jobs import views

urlpatterns = [
    # 职位列表
    # path("joblist/", views.joblist, name="joblist"),
    url(r"^joblist/",views.joblist, name="joblist"),
    url(r"^job/(?P<job_id>\d+)/$",views.detail, name="detail"),



]
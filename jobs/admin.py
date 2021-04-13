from django.contrib import admin
from jobs.models import Job
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    """
    显示列表页特定字段
    """
    exclude = ('creator','created_date','modified_date')
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')

    def save_model(self, request, obj, form, change):
        """
        把职位的创建人设计成当前登录的用户
        """
        if obj.creator is None:
            obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Job,JobAdmin)

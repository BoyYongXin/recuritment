from django.shortcuts import render
from django.http import Http404
# Create your views here.
from jobs.models import Job

from jobs.models import Cities, JobTypes
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin # 继承多个类
from django.views.generic.edit import CreateView
from jobs.models import Resume

import logging

logger = logging.getLogger(__name__)

# def joblist(request):
#     job_list = Job.objects.order_by('job_type')
#     template = loader.get_template("joblist.html")
#     context =  {'job_list': job_list}
#     for job in job_list:
#         job.city_name = Cities[job.job_city][1]
#         job.type_name = JobTypes[job.job_type][1]
#     # return render(request, 'joblist.html', context)
#     return HttpResponse(template.render(context))

def joblist(request):
    """
     职位详情列表页面
    :param request:
    :return:
    """
    job_list = Job.objects.order_by('job_type')
    context =  {'job_list': job_list}
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]
    return render(request, 'joblist.html', context)

def detail(request, job_id):
    """
    职位详情页面
    :param request:
    :param job_id:
    :return:
    """

    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
        logger.info('job retrieved from db :%s' % job_id)
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, 'job.html', {'job': job})

class ResumeCreateView(LoginRequiredMixin, CreateView):
    """    简历职位页面  """
    template_name = 'resume_form.html'
    success_url = '/joblist/'
    model = Resume
    fields = ["username", "city", "phone",
        "email", "apply_position", "gender",
        "bachelor_school", "master_school", "major", "degree", "picture", "attachment",
        "candidate_introduction", "work_experience", "project_experience"]

    ### 从 URL 请求参数带入默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    def form_valid(self, form):
        """
        验证表单
        :param form:
        :return:
        """
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

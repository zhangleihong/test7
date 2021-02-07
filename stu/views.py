from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import registerStu


def index_view(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        sname = request.POST.get('sname','')
        cname = request.POST.get('clsname','')
        coursenames = request.POST.getlist('coursename',[])

        flag = registerStu(sname,cname,*coursenames)
        if flag:
            return HttpResponse('注册成功！')
        else:
            return HttpResponse('注册失败！')

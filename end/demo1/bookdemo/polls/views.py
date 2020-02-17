from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
# Create your views here.
from django.views.generic import View,TemplateView,ListView,CreateView,DeleteView,UpdateView,DetailView
# View类为所有的视图响应类的父类


def index(request):
    questions = Question.objects.all()
    # 使用render发起一次请求
    return render(request,'polls/index.html',{"questions":questions})
    # return HttpResponse("首页")

# 基于CBV的形式实现首页
class IndexView(ListView):
    # 方法二、继承ListView
    # template_name指明使用的模板
    template_name = "polls/index.html"
    # queryset 指明返回的结果列表
    queryset = Question.objects.all()
    # context_object_name 指明返回字典参数的健
    context_object_name = "questions"

    # 方法一、继承的TemplateView
    # template_name = "polls/index.html"
    # def get_context_data(self, **kwargs):
    #     return {"questions":Question.objects.all()}





def detail(request, qid):
    print(qid, "+++")
    if request.method == "GET":
        try:
            question = Question.objects.get(id=qid)
            print(question, "--")
            # 使用render发起一起请求
            return render(request, 'polls/detail.html', {"question": question})

        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")
    elif request.method == "POST":
        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes+=1
            choice.save()
            # 返回当前投票问题的投票结果页
            url = reverse("polls:result", args=(qid,))
            # 投票成功 返回投票结果

            # redirect其实没有真正的返回内容   而是让浏览器重新请求一个地址
            # 不能反复刷新post的结果
            # question = Question.objects.get(id=qid)
            # 错误的结局  刷新页面导致数据出错
            # return render(request,'polls/result.html',{"question":question})
            return redirect(to=url)
            # return HttpResponse("投票成功了")  #接受了详情页的post请求
            # return HttpResponse("现在我代替你进入到了投票结果页")  # 接受了结果页的get请求

        except:
            return HttpResponse("选项不合法")



    # return HttpResponse("详情页"+qid)

class DetailView(DetailView):
    template_name = "polls/index.html"

def result(request,qid):

    try:
        question = Question.objects.get(id=qid)
        return render(request,'polls/result.html',{"question":question})
    except Exception as e:
        print(e)
        return HttpResponse("问题不合法")
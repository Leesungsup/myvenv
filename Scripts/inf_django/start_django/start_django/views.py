#뷰 기능을 담당
#화면이 나타나느 뷰(template가 있음), 화면이 없는 뷰
#URL은 항상 필요
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    html="<html><body>Hi</body></html>"
    return HttpResponse(html)

def welcome(request):
    html="<html><body>welcome to Django</body></html>"
    return HttpResponse(html)

def template_test(request):
    #기본템플릿 폴 1. admin 앱 2. 각 앱의 폴더에 있는 template폴더 3. 우리가 설정한폴더
    return render(request,'test.html')

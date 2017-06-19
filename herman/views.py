#coding:utf-8
from django.http import HttpResponse

def index(request):
    return HttpResponse(u"Hello,小丸子")

# Create your views here.

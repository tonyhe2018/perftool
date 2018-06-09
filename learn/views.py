from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request,):
    return HttpResponse(u'welcome to chongqing middle-school!')

def add(request,):
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
    sum = int(a) + int(b)
    return HttpResponse(str(sum))

def add2(request, a, b,):
    print(a,b)
    sum = int(a) + int(b)
    return HttpResponse(str(sum))

def home(request,):
    return render(request,'home.html')


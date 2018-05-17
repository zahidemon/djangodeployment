from django.shortcuts import render

# Create your views here.
def index(request):
    c={'text':'Hello World','Age':20}
    return render(request,'index.html',c)

def other(request):
        return render(request,'other.html')

def relative(request):
    return render(request,'relative_url.html')

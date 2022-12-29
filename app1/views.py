from django.shortcuts import render

# Create your views here.
def jinja_print1(request):
    d={'name':'sowmya'}
    return render(request,'jinja_print1.html',context=d)
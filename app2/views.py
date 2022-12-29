from django.shortcuts import render

# Create your views here.
def jinja_print2(request):
    d={'username':'chinna'}
    return render(request,'jinja_print2.html',d)
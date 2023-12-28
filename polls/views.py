from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def home (request):
    backVar="Hello"
    a="Je suis la plus belle et la plus intelligente"
    data={'student1':1,'student2':2, 'student3':3}
    context={"frontVar":backVar,"khaled": a,"List1":[1,2,3,4,5], 'data':data}
    return render (request,"index.html", context)

def chart(request):
    context = {
        "labels" : [ "Student" + str(i+1) for i in range(6)],
        "data" : [0, 0, 30, 50, 20, 30]
                 }
    return render(request, "chart.html", context)

def page(request):
    context = {
        "earnings" : "140.000 $"
    }
    return render(request, "chart_page.html", context)

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



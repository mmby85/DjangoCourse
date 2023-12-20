from django.shortcuts import render
from django.http import HttpResponse
import random
# from db import get_fake_news
from .models import News
from .forms import NewsForm

def index(request):
    r = random.randint(0,10000)
    return HttpResponse(f"<h1>Hello, world. You're at the Predict Fake Application {r}.</h1>")

def home(request):
    # data = get_fake_news()
    return render(request, "home.html")

def show_news(request):

    all_news = News.objects.all()

    context = {
        "news" : [ [article.id, article.keywords, article. lang, article.country  ] for article in all_news]
    }

    return render(request, "home.html", context=context)

def fill_news(request):

    forms = NewsForm()

    if request.method == "POST" :
        forms = NewsForm(request.POST)
        if forms.is_valid() :
            forms.save()
        print(request.POST)

    return render(request, "forms.html", context= {"forms" : forms})
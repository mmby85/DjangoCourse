from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Home</h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('predictfake/', include("predictfake.urls")),
    path('' , index),
]

from django.shortcuts import render
from .data_analysis import result

def chart(request):
    context = {
        "labels" : list(result["brand"].keys()),
        "data" : list(result["brand"].values())
                 }
    print(context)
    return render(request, "data_chart.html", context)
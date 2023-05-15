from django.shortcuts import render, HttpResponse

# Create your views here.


def chat(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def chatAPI(request):
    return HttpResponse("This works")

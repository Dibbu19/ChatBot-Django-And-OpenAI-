from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import openai

openai.api_key = "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"


# Create your views here.


def chat(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def chatAPI(request):
    if request.method == "POST":
        prompt = request.POST["prompt"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response)
        return JsonResponse(response)
    return HttpResponse("Bad Request")

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import openai

<<<<<<< HEAD
openai.api_key = ""  # type your OpenAI Secret Key Here
=======
openai.api_key = "" //type your OpenAI secret key here
>>>>>>> a6d22755ec50ee4410784308ecacab98949a02b8


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

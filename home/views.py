from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import openai

<<<<<<< HEAD
openai.api_key = ""  # type your OpenAI secret key here
=======
openai.api_key = ""
>>>>>>> ae2824b85fb38204510d31f5be55ec5af2b046f2


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

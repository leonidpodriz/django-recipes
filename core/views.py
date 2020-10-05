from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def homepage(request: HttpRequest) -> HttpResponse:
    user = request.user

    context = {
        "welcome_message": f"Hello, {user}!",
    }
    
    return render(request, "homepage.html", context=context)

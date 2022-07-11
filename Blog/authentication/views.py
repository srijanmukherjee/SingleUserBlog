from django.http import HttpRequest, HttpResponse


def auth(request: HttpRequest):
    return HttpResponse("you are in the /auth route")

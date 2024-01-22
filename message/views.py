from django.http import HttpResponse


def message_view(request):
    return HttpResponse("<h1>Hello Django!</h1>")

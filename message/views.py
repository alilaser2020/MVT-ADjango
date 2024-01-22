from django.shortcuts import render


def view_message(request):
    return render(request, 'home.html')

from django.http import HttpResponse


def index(request):
    return HttpResponse('Даже не верится')


def second_page(request):
    return HttpResponse('А это вторая страница!')

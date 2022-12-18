from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIGKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+-=')
    if request.GET.get('numbers'):
        characters.extend('1234567890')

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(
        request,
        'generator/password.html',
        {'password': thepassword}
        )


def description(request):
    return render(request, 'generator/description.html')

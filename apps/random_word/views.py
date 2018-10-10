from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1

    word = get_random_string(length=14)
    context = {'word': word}

    return render(request, 'random_word/index.html', context)

def reset(request):
    if 'counter' in request.session:
        del request.session['counter']
        
    return redirect('/')
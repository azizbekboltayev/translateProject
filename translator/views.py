from django.shortcuts import render
from django.http import HttpResponse
# from .models import Dictionary
from translate import Translator

def index(request):
    if request.method == 'POST':

        text = request.POST['translate']
        to_lang = request.POST['tolanguage']
        from_lang = request.POST["fromlanguage"]
        translator = Translator(to_lang=to_lang, from_lang=from_lang)
        translation = translator.translate(text)

        context = {
            'translation': translation,
            'text': text,
        }
        return render(request,'index.html', context)
    return render(request, 'index.html')

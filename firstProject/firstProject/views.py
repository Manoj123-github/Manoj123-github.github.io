
# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import ensure_csrf_cookie

import firstProject.pmodel as PModel

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        return render(request, 'index.html', params)

    else:
        ptext={'none_analyzed_text':djtext}
        return render(request,'index.html',ptext)


def predict(request,slug):
    print(slug)

    predicition = PModel.score_output(slug, fact = 0.4)
    print(predicition)
    data = {}
    return JsonResponse(predicition,safe=False)
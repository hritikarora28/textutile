from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("hello world")
def index(request):

     return  render(request, 'index.html')



def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    # check box
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')




    if removepunc == "on":


        puncuation = '''!()-[];:"\<>/?@#$%^&*_~'''
        analyzed = ""
        # her the loop is used to check the puncuation in the text
        for char in djtext:
            if char not in puncuation:
                   analyzed = analyzed + char

        params = {'purpose':'Remove Puncuation', 'analyzed_text': analyzed}
        djtext = analyzed



    if(fullcaps == "on"  ):
        analyzed = ""
        for char in djtext:
           analyzed = analyzed+char.upper()
        params = {'purpose': 'change to upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == "on" ):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed
    if (removepunc== "off" and fullcaps== "off" and newlineremover== "off"):
        return HttpResponse("PLEASE SELECT  ANY ONE OPTION")





    return render(request, 'analyze.html', params)

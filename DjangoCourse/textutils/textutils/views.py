# I have created this file - Nisarg

from django.http import HttpResponse
from django.shortcuts import render

# PERSONAL NAVIGATOR

# def navigation(request):
#     return HttpResponse('''<h1>Navigation bar</h1> <a Href = "https://www.facebook.com/login/">Facebook Login</a><br>
#     <a Href = "https://www.instagram.com/accounts/login/?hl=en">\Instagram Login</a><br>
#     <a Href = "https://twitter.com/login?lang=en">\Twitter Login</a><br>''')

# LAYING THE PIPELINE

# def index(request):
#     return HttpResponse('''<h1>Home</h1> <a Href = "http://127.0.0.1:8000/removepunc">Removepunc</a><br>
#     <a Href = "http://127.0.0.1:8000/capitalizefirst">Capitalizefirst</a><br>
#     <a Href = "http://127.0.0.1:8000/newlineremove">Newlineremove</a><br>
#     <a Href = "http://127.0.0.1:8000/spaceremove">Spaceremove</a><br>
#     <a Href = "http://127.0.0.1:8000/charcount">Charcount</a><br>''')
#
# def removepunc(request):
#     return HttpResponse('''<h1>removepunc</h1> <a Href = '/'>Back</a><br>''')
#
# def capitalizefirst(request):
#     return HttpResponse('''<h1>capitalizefirst</h1> <a Href ='/'>Back</a><br>''')
#
# def newlineremove(request):
#     return HttpResponse('''<h1>newlineremove</h1> <a Href ='/'>Back</a><br>''')
#
# def spaceremove(request):
#     return HttpResponse('''<h1>spaceremove</h1> <a Href ='/'>Back</a><br>''')
#
# def charcount(request):
#     return HttpResponse('''<h1>charcount</h1> <a Href ='/'>Back</a><br>''')

# TEMPLATES

# def index(request):
#      dict = {'Name':'Nisarg', 'Place':'India'}
#      return render(request, 'index.html', dict)

# CREATING HOMEPAGE OF OUR TEXTUTILS WBSITE

# def index(request):
#     return render(request, 'index.html')
#
# def removepunc(request):
#      # GET THE TEXT
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#      # ANALIZE THE TEXT
#     return HttpResponse('removepunc')

# BACKEND CODING

# def index(request):
#     return render(request, 'index.html')
#
# def analyze(request):
#     #Get the text
#     djtext = request.GET.get('text', 'default')
#
#     # Check checkbox values
#     removepunc = request.GET.get('removepunc', 'off')
#     fullcaps = request.GET.get('fullcaps', 'off')
#     NewLineRemover = request.GET.get('NewLineRemover', 'off')
#     ExtraSpaceRemover = request.GET.get('ExtraSpaceRemover', 'off')
#     CharCounter = request.GET.get('CharCounter', 'off')
#
#     #Check which checkbox is on
#     if removepunc == "on":
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
#         #Analyze the text
#         return render(request, 'analyze.html', params)
#
#     elif fullcaps == "on":
#         analyzed = ""
#         for char in djtext:
#             analyzed = analyzed + char.upper()
#         params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
#         # Analyze the text
#         return render(request, 'analyze.html', params)
#
#     elif NewLineRemover == "on":
#         analyzed = ""
#         for char in djtext:
#             if char != "\n":
#                analyzed = analyzed + char
#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
#         # Analyze the text
#         return render(request, 'analyze.html', params)
#
#     elif ExtraSpaceRemover == "on":
#         analyzed = ""
#         for index, char in enumerate(djtext):
#             if not(djtext[index] == " " and djtext[index+1] == " "):
#                analyzed = analyzed + char
#         params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
#         # Analyze the text
#         return render(request, 'analyze.html', params)
#
#     elif CharCounter == "on":
#         analyzed = ""
#         for char in djtext:
#             analyzed = analyzed + char
#         counter = len(djtext)
#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed, 'Characters': counter}
#         # Analyze the text
#         return render(request, 'analyze.html', params)
#
#     else:
#         return HttpResponse("Error")

# BUG FIXING(ALL CHEACKBOXES ARE ON)

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    NewLineRemover = request.GET.get('NewLineRemover', 'off')
    ExtraSpaceRemover = request.GET.get('ExtraSpaceRemover', 'off')
    CharCounter = request.GET.get('CharCounter', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        #Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (NewLineRemover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if ExtraSpaceRemover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
               analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if CharCounter == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char
        counter = len(djtext)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed, 'Characters': counter}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (removepunc != "on" and NewLineRemover != "on" and ExtraSpaceRemover != "on" and fullcaps != "on" and CharCounter != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

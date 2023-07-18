from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request ,'index.html')

def about(request):
    return render(request ,'about.html')

def analyze(request):
    djtext = request.POST.get("text","default")
    print(djtext)
    remove_punc = request.POST.get("removepunc","off")
    print(remove_punc)
    removeextraspace = request.POST.get("removeextraspace","off")
    capitalize = request.POST.get("capitalize","off")
    newlineremover = request.POST.get("newlineremover","off")
    charcount = request.POST.get("charcount","off")

    if remove_punc!='on' and capitalize!='on' and removeextraspace!='on' and charcount!='on' and newlineremover!='on':
        analyzed_text=djtext
        params = {"purpose":"NONE",
            "analyzed_text":analyzed_text}
        return render(request,"analyze.html",params)
    
    if remove_punc == 'on':
        analyzed_text =''
        punc_list = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punc_list:
                analyzed_text=analyzed_text+char
            params = {"purpose":"Remove Punctuations",
              "analyzed_text":analyzed_text}
        djtext=analyzed_text
    
    if newlineremover == 'on':
        analyzed_text =''
        for char in djtext:
            if char != "\n" and char!='\r':
                analyzed_text=analyzed_text+char
            params = {"purpose":"new line remover",
              "analyzed_text":analyzed_text}
        djtext=analyzed_text
    
    if capitalize == 'on':
        analyzed_text =''
        
        for char in djtext:
            
            analyzed_text=analyzed_text+(char.upper())
            params = {"purpose":"CAPITALIZE",
              "analyzed_text":analyzed_text}
        djtext=analyzed_text
    if removeextraspace == 'on':
        analyzed_text =''
        length=len(djtext)
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' ' ):
                analyzed_text=analyzed_text+char
            params = {"purpose":"extra space remover",
              "analyzed_text":analyzed_text}
        djtext=analyzed_text
    
    if charcount == 'on':
        charno =len(djtext)
        params = {"purpose":"extra space remover",
              "analyzed_text":f"YOUR DESIRED TEXT HAS {charno} CHARACTERS \n'{djtext}' "}
        
    
    return render(request,"analyze.html",params)
    
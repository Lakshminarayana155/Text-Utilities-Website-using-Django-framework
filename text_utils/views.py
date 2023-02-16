from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home-2.htm')


def removepunctuations(request):
    inputtext=request.POST.get('text','default')
    removepunctuations = request.POST.get('removepunctuations','off')
    capitalize = request.POST.get("capitalize","off")
    spaceremover=request.POST.get("spaceremover",'off')
    analysed=inputtext
    if removepunctuations=='on':
        punctuations = "!@#$%^&*()_+-=\|[]{\"':;}/?><"
        analysed=""
        for ch in inputtext:
            if ch not in punctuations:
                analysed+=ch

    if capitalize=='on':
        analysed=analysed.upper()

        

    if spaceremover == 'on':
        f_analysed=""
        for i,ch in enumerate(analysed):
            if not(analysed[i]==" " and analysed[i+1] == " "):
                f_analysed+=ch
        analysed=f_analysed
    
    context={
        "analysed":analysed,
    }

    return render(request,"analysed-2.htm",context)   
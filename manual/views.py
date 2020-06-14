from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def List(request):
    return render(request,"list.html")

def napkin(request):
    return render(request,"napkin.html")

def pcover(request):
    return render(request,"pillowCover.html")

def slip(request):
    return render(request,"slip.html")

def shimmi(request):
    return render(request,"shimmi.html")

def ufrock(request):
    return render(request,"ufrock.html")

def inskirt(request):
    return render(request,"inskirt.html")

def nightie(request):
    return render(request,"nightie.html")

def salwar_pant(request):
    return render(request,"salwar_pant.html")

def gpant(request):
    return render(request,"gpant.html")
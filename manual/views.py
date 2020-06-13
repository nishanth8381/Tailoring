from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def List(request):
    return render(request,"list.html")

def napkin(request):
    return render(request,"napkin.html")
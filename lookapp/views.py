from django.shortcuts import render

def home(request):
    return render(request,"home.html",{})
def O_mnie(request):
    return render(request,"O_mnie.html",{})
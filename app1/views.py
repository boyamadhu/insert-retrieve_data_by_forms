from django.shortcuts import render

# Create your views here.
def brother(request):
    return render(request,'fourth.html')

def sister(request):
    return render(request,'third.html')

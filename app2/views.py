from django.shortcuts import render

# Create your views here.
def mom(request):
    return render(request,'first.html')

def dad(request):
    return render(request,'second.html')
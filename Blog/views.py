from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return render(request,'blog.html')

def detay_atik1(request):
    return render(request,'Atik1.html')

def detay_atik2(request):
    return render(request,'atik2.html')

def detay_atik3(request):
    return render(request,'atik3.html')
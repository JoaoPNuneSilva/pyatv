from django.shortcuts import render

# Create your views here.

def pag1 (request):
    return render(request, 'pag1.html')
def pag2 (request):
    return render(request, 'pag2.html')
def pag3 (request):
    return render(request, 'pag3.html')
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def portfolio(request):
    return render(request, 'portfolio.html')

from django.shortcuts import render

def portfolio(request):
    return render(request, 'portfolio.html')

def skills(request):
    return render(request, 'skills.html')

def about(request):
    return render(request, 'about.html')

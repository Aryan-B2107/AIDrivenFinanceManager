from django.shortcuts import render

def dashboard(request):
    return render(request, 'transactions/dashboard.html')

def leaderboard(request):
    return render(request, 'transactions/leaderboard.html')

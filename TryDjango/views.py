from django.shortcuts import render

def home(request):
    context = {
        'name': 'Imran',
        'age' : 24,
        'city' : 'Dhaka'
    }
    return render(request, 'TryDjango/home.html', context)

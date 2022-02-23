from django.shortcuts import render

def counter(request):
    return render(request, 'counter\counter.html', {})

# Create your views here.

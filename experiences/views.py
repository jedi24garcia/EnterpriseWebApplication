from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def search(request):
    query = request.GET.get('q')
    return render(request, 'search_results.html', {'query': query})

@login_required
def home(request):
    return render(request, 'base.html')
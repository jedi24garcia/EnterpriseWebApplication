from django.shortcuts import render

# Create your views here.
def search(request):
    query = request.GET.get('q')
    return render(request, 'search_results.html', {'query': query})

def home(request):
    return render(request, 'home.html')


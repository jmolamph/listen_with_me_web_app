from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):
    # renders the index template we have
    return render(request, 'frontend/index.html')
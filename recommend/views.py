from django.shortcuts import render
from .models import Review

# Create your views here.
def topfive(request):
    recommend = Review.objects.all().order_by('-recommend')
    recommend = recommend[:5]
    return render(request, 'topfive.html', {'recommend':recommend})
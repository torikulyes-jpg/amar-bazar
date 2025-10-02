from django.shortcuts import render
from ads.models import Ad

def home(request):
    latest_ads = Ad.objects.filter(is_active=True).order_by('-created_at')[:8]
    context = {
        'latest_ads': latest_ads
    }
    return render(request, 'home.html', context)

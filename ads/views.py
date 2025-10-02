from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Ad, Category
from .forms import AdForm

def ad_list(request):
    ads = Ad.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.all()
    
    category_id = request.GET.get('category')
    if category_id:
        ads = ads.filter(category_id=category_id)
    
    query = request.GET.get('q')
    if query:
        ads = ads.filter(title__icontains=query)
    
    context = {
        'ads': ads,
        'categories': categories,
    }
    return render(request, 'ads/ad_list.html', context)

def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, is_active=True)
    context = {
        'ad': ad
    }
    return render(request, 'ads/ad_detail.html', context)

@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.seller = request.user
            ad.save()
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = AdForm()
    return render(request, 'ads/create_ad.html', {'form': form})

@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, seller=request.user)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/edit_ad.html', {'form': form, 'ad': ad})

@login_required
def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, seller=request.user)
    if request.method == 'POST':
        ad.is_active = False
        ad.save()
        return redirect('ad_list')
    return render(request, 'ads/delete_ad.html', {'ad': ad})

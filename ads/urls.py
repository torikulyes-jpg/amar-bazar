from django.urls import path
from . import views

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('create/', views.create_ad, name='create_ad'),
    path('<int:ad_id>/edit/', views.edit_ad, name='edit_ad'),
    path('<int:ad_id>/delete/', views.delete_ad, name='delete_ad'),
]

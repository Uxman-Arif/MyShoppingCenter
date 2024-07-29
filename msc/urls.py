from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.viewsfnc, name='my-shopping-center'),
    path('about/', views.about, name='about'),
    path('contact/', views.contacts, name='contact'),
    path('tracker/', views.tracker, name='tracker'),
    path('productview/<int:id>/', views.productview, name='productview'),
    path('search/', views.search, name='search'),
    path('checkout/', views.checkout, name='checkout'),
]